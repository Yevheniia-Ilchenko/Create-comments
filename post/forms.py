from django import forms
from captcha.fields import CaptchaField
from post.models import Comment


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ["user", "email", "home_page", "comment_text", ]
