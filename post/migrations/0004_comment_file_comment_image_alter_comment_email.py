# Generated by Django 5.0.3 on 2024-06-13 10:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0003_comment_email_comment_home_page"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to="comment_files/"),
        ),
        migrations.AddField(
            model_name="comment",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="comment_images/"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="email",
            field=models.EmailField(
                default="new@gmail.com",
                max_length=254,
                validators=[django.core.validators.EmailValidator()],
            ),
        ),
    ]
