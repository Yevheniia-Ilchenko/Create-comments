from django import forms
from captcha.fields import CaptchaField
from django.utils.html import strip_tags

from post.models import Comment


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ["user", "email", "home_page", "comment_text", ]

    def clean_comment_text(self):
        text = self.cleaned_data.get('comment_text')
        allowed_tags = ['b', 'i', 'u', 'a']
        return strip_tags(text, allowed_tags)
