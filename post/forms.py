from django import forms

from post.models import Comment


class CommentForm(forms.ModelForm):
    # captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = "__all__"
