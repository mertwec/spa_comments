from django.shortcuts import render, redirect
from comments.models import MockPost, Comment
from comments.forms import NewCommentForm
from comments.tools import split_on_pages

import pdb


def block_comments(request):

    post = MockPost.objects.first()
    if not post:
        post = MockPost.objects.create(title='Discussion')

    form = NewCommentForm()

    if request.method == "POST":
        form = NewCommentForm(request.POST)
        pdb.set_trace()
        if form.is_valid():
            new_comm = form.save(commit=False)
            new_comm.post_id = post.pkc
            new_comm.parrent_id = form["parent"].value()
            new_comm.save()
            return redirect('/')

    all_comments = Comment.objects.all()
    zero_comments = Comment.objects.all().filter(level=0)
    items_on_page = 25
    page = split_on_pages(
        request=request,
        queryset=all_comments,
        items_on_page=items_on_page)

    # pdb.set_trace()
    return render(
        request,
        template_name="comments/content.html",
        context={
            "title": post.title,
            "comments": page.object_list,
            # "all_comments": all_comments,
            "page": page,
            "comment_form": form
        }
    )
