from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from post.models import Comment, User

admin.site.register(Comment)
admin.site.register(User, UserAdmin)
