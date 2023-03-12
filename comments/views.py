from django.shortcuts import render


def block_comments(request):
    return render(
        request,
        template_name="base.html",
        context={
            "title": "Comments"
        }
    )
