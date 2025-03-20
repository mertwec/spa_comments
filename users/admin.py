from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.forms import ChangeForm, RegisterForm
from users.models import CustomUser

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = ChangeForm
    model = User
    list_display = ["username", "email", "is_superuser", "date_joined"]


admin.site.register(CustomUser, CustomUserAdmin)
