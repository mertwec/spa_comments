from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page
from django.http import HttpRequest


def split_on_pages(request:HttpRequest, queryset, items_on_page=5)-> Page:
    paginator = Paginator(queryset, items_on_page)
    page = request.GET.get("page", 1)
    try:
        set_to_page = paginator.page(page)
    except PageNotAnInteger:
        set_to_page = paginator.page(1)
    except EmptyPage:
        set_to_page = paginator.page(paginator.num_pages)
    
    return set_to_page
