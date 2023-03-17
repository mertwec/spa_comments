from django.shortcuts import redirect
from django.urls import reverse


def main_redirect_sort(request):
    url = reverse("comments:sorted_page", kwargs={"sorter":"-created_on"})
    # import pdb; pdb.set_trace()
    return redirect(url)
