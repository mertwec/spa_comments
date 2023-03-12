from django.urls import path
from comments import views

app_name = "comments"

urlpatterns = [
    path('/', views.block_comments, name="comments"),
]
