import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page
from django.http import HttpRequest
from captcha.models import CaptchaStore


def split_on_pages(request: HttpRequest, queryset, items_on_page=5) -> Page:
    """split queryset on pages
    """
    paginator = Paginator(queryset, items_on_page)
    page = request.GET.get("page", 1)
    try:
        set_to_page = paginator.page(page)
    except PageNotAnInteger:
        set_to_page = paginator.page(1)
    except EmptyPage:
        set_to_page = paginator.page(paginator.num_pages)

    return set_to_page


def get_captcha_key() -> str:
    """ get random hashkey from table 'CaptchaStore'.
    if table is empty -- generate 10 keys.
    """
    captcha_keys = CaptchaStore.objects.only("hashkey")
    if not captcha_keys:
        CaptchaStore.create_pool(10)
        captcha_keys = CaptchaStore.objects.only("hashkey")
    return random.choice(captcha_keys).hashkey
