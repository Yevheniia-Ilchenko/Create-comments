import os
import uuid
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, URLValidator
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.text import slugify


class User(AbstractUser):
    class Meta:
        ordering = ["username", ]


def upload_image_file(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.user)}-{uuid.uuid4()}{extension}"

    return os.path.join("comment_image/", filename)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="comments")
    email = models.EmailField(validators=[EmailValidator()])
    home_page = models.URLField(blank=True,
                                null=True,
                                validators=[URLValidator()])
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey("self",
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE,
                               related_name="replies")
    image = models.ImageField(upload_to=upload_image_file,
                              blank=True,
                              null=True)
    file = models.FileField(upload_to=upload_image_file,
                            blank=True,
                            null=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        self.comment_text = strip_tags(self.comment_text)
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 320 or img.width > 240:
                output_size = (320, 240)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.created_at}"
