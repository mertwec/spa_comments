from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.urls import reverse
from comments.models import MockPost, Comment
from comments import forms as com_form
from comments.tools import split_on_pages, get_captcha_key

import pdb


@never_cache
def block_comments(request, sorter):
    if sorter not in ["username", "email", "created_on", "-created_on"]:
        sorter = "-created_on"

    post = MockPost.objects.first()
    if not post:
        post = MockPost.objects.create(title='Discussion')

    if request.user.is_authenticated:
        form = com_form.AuthCommentForm()
    else:
        form = com_form.AnonimCommentForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = com_form.AuthCommentForm(request.POST)
        else:
            form = com_form.AnonimCommentForm(request.POST)
        if form.is_valid():
            new_comm = form.save(commit=False)
            if isinstance(form, com_form.AuthCommentForm):
                new_comm.username = request.user.username
                new_comm.email = request.user.email

            new_comm.post_id = post.pk
            new_comm.save()
            page = request.GET.get("page", 1)
            url = reverse("comments:sorted_page", kwargs={"sorter": sorter})
            return redirect(f'{url}?page={page}')

    all_comments = Comment.objects.all()

    # get all comments higher level
    zero_comments = all_comments.filter(
        level=0).order_by(sorter, "-created_on")

    items_on_page = 10
    page = split_on_pages(
        request=request,
        queryset=zero_comments,
        items_on_page=items_on_page)

    # add subcomments to zero comments on page
    page_tree_comments = [all_comments.filter(
        tree_id=i.tree_id) for i in page.object_list]

    all_count = sum(map(len, page_tree_comments))
    # pdb.set_trace()
    return render(
        request,
        template_name="comments/content.html",
        context={
            "title": post.title,
            "comments": page_tree_comments,
            "page": page,
            "comment_form": form,
            "count_main": items_on_page,
            "count_all": all_count,
            "zero_count": len(page_tree_comments)
        }
    )


@never_cache
def reply_form_comment(request, comment_id=None):
    form = com_form.AnonimCommentForm()
    if request.user.is_authenticated:
        form = com_form.AuthCommentForm()
    form.initial["parent"] = comment_id

    # form.initial["text"] = f"answer for {comment_id}"
    return render(request, "comments/nodes/form_new_comment.html", {"comment_form": form})


# method delete
def delete_comment(request, id, sorter='-created_on'):
    del_obj = get_object_or_404(Comment, pk=id)
    del_obj.delete()
    return redirect(reverse("comments:sorted_page", kwargs={"sorter": sorter}))
