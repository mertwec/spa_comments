from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from comments import models

admin.site.register(models.MockPost)
# admin.site.register(models.User)
admin.site.register(models.Comment, MPTTModelAdmin)
