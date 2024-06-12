from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from post.models import Comment, User


class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "comment_text", "created_at", ]


admin.site.register(Comment, CommentAdmin)
admin.site.register(User, UserAdmin)
