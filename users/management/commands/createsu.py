from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from SPA_application.settings import ADMIN_USER

User = get_user_model()


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        if not User.objects.filter(username=ADMIN_USER["login"]).exists():
            User.objects.create_superuser(
                username=ADMIN_USER["login"],
                password=ADMIN_USER["password"],
            )
            print("Superuser has been created.")
            return
        print("Superuser already is exists.")
