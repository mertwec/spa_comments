from django.shortcuts import render, redirect
from comments.models import MockPost, Comment
from comments.forms import NewCommentForm
from comments.tools import split_on_pages, get_captcha_key

import pdb


def main_redirect_sort(request):
    return redirect("/-created_on")


def block_comments(request, sorter):
    if sorter not in ["username", "email", "created_on", "-created_on"]:
        sorter = "-created_on"
    post = MockPost.objects.first()
    if not post:
        post = MockPost.objects.create(title='Discussion')

    form = NewCommentForm()

    if request.method == "POST":
        form = NewCommentForm(request.POST)
        # pdb.set_trace()
        if form.is_valid():
            new_comm = form.save(commit=False)
            new_comm.post_id = post.pk
            new_comm.parrent_id = form["parent"].value()
            new_comm.save()
            page = request.GET.get("page", 1)
            return redirect(f'/{sorter}/?page={page}')
        else:
            form = NewCommentForm(request.POST)

    all_comments = Comment.objects.all()
    # get all comments higher level

    zero_comments = all_comments.filter(
        level=0).order_by(sorter, "-created_on")

    items_on_page = 10
    page = split_on_pages(
        request=request,
        queryset=zero_comments,
        items_on_page=items_on_page)

    # add subcomments to zero comeents on page
    page_tree_comments = [all_comments.filter(
        tree_id=i.tree_id) for i in page.object_list]

    # pdb.set_trace()
    all_count = sum(map(len, page_tree_comments))
    captcha_key = get_captcha_key()

    return render(
        request,
        template_name="comments/content.html",
        context={
            "title": post.title,
            "comments": page_tree_comments,
            "page": page,
            "comment_form": form,
            "ckey": captcha_key,
            "count_main": items_on_page,
            "count_all": all_count
        }
    )
