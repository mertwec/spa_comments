"""SPA_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache
from SPA_application import settings, views
import pprint as pp

import django.contrib.auth.urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', include('users.urls')),
    # path('users/', include('django.contrib.auth.urls')), # default urls for CRUD user

    path('', views.main_redirect_sort, name="home"),
    path('captcha/', include('captcha.urls')),
    path('comments/', include('comments.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))

