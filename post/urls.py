from django.urls import path
from .views import CommentListView


urlpatterns = [
    path("", CommentListView.as_view(), name="comment-list"),
]

app_name = "post"
