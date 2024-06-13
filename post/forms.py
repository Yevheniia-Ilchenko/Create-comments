from django import forms
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from post.models import Comment


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()
    image = forms.ImageField(required=False)
    file = forms.FileField(required=False)

    class Meta:
        model = Comment
        fields = ["user",
                  "email",
                  "home_page",
                  "comment_text",
                  "parent",
                  "image",
                  "file"]

    # def clean_comment_text(self):
    #     text = self.cleaned_data.get("comment_text")
    #     allowed_tags = ["b", "i", "u", "a"]
    #     return strip_tags(text, allowed_tags)

    def clean_file(self):
        file = self.cleaned_data.get("file")

        if file:
            if file.content_type not in ["image/jpeg", "image/png", "image/gif", "text/plain"]:
                raise ValidationError("Invalid file format. Acceptable formats: JPG, GIF, PNG, TXT.")

            if file.content_type == "text/plain" and file.size > 100 * 1024:
                raise ValidationError("The text file size should not exceed 100 kb.")

        return file

    def clean_image(self):
        image = self.cleaned_data.get("image")

        if image:
            if image.size > 320 * 240:
                raise ValidationError("The image is too large. Acceptable size: 320x240 pixels.")

        return image
