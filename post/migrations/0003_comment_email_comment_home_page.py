# Generated by Django 5.0.6 on 2024-06-12 21:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0002_comment_parent"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="email",
            field=models.EmailField(
                max_length=254,
                null=True,
                validators=[django.core.validators.EmailValidator()],
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="home_page",
            field=models.URLField(
                blank=True,
                null=True,
                validators=[django.core.validators.URLValidator()],
            ),
        ),
    ]
