# Generated by Django 4.1.7 on 2023-03-13 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="owner_id",
        ),
        migrations.AddField(
            model_name="comment",
            name="email",
            field=models.EmailField(default="anon@ex.com", max_length=254),
        ),
        migrations.AddField(
            model_name="comment",
            name="username",
            field=models.CharField(default="Anonim", max_length=50),
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
