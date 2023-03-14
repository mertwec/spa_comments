from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MockPost(models.Model):
    title = models.CharField(max_length=50, default="Comments")

    def __str__(self) -> str:
        return f'Mpost: {self.title}'


class Comment(MPTTModel):
    """comments to post"""
    post = models.ForeignKey(
        MockPost, related_name='comments', on_delete=models.CASCADE)
    
    username = models.CharField(max_length=50, null=False, default="Anonim")
    email = models.EmailField(null=False, default="anon@ex.com")
    
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                                   on_delete=models.CASCADE)

    text = models.TextField(null=False, blank=False)
    url = models.URLField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    class MpttMeta:
        order_insertion_by = ['created_on']
        db_table = 'comments'
    
    def __str__(self):
        return f"comment {self.username}:  {self.text}"


# class User(models.Model):
#     username = models.CharField(max_length=50, null=False)
#     email = models.EmailField(null=False)
    
#     def __str__(self) -> str:
#         return f'user: {self.username}'


# class Post(models.Model):
#     title = models.CharField(max_length=50, default="Comments")
#     text = models.TextField(null=False, blank=False)
#     url = models.URLField(null=True, blank=True)

#     owner = models.ForeignKey(
#         User, related_name='posts', on_delete=models.CASCADE)

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return f'Post: {self.title} owner {self.owner}'


# class Comment(MPTTModel):

#     post = models.ForeignKey(
#         Post, related_name='comments', on_delete=models.CASCADE)
    
#     owner = models.ForeignKey(
#         User, related_name='comments', on_delete=models.CASCADE)
    
#     parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
#                                    on_delete=models.CASCADE)

#     text = models.TextField(null=False, blank=False)
#     url = models.URLField(null=True, blank=True)

#     created_at = models.DateTimeField(auto_now_add=True)

#     class MpttMeta:
#         order_insertion_by = ['created_on']
#         db_table = 'comments'
    
#     def __str__(self):
#         return f"comment {self.username}:  {self.text}"
