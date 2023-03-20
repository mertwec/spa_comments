from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.username}, admin:{self.is_superuser}"
