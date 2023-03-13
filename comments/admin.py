from django.contrib import admin
from comments import models
from mptt.admin import MPTTModelAdmin


admin.site.register(models.MockPost)
# admin.site.register(models.User)
admin.site.register(models.Comment, MPTTModelAdmin)
