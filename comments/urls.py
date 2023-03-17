from django.urls import path
from comments import views

app_name = "comments"   # пространство имен

urlpatterns = [
    path('<str:sorter>/', views.block_comments, name="sorted_page"),
    path('delete/<int:id>/', views.delete_comment, name='delete_comment')
]
