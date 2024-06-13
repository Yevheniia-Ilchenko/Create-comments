from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import CommentListView, CommentCreateView

urlpatterns = [
    path("", CommentListView.as_view(), name="comment-list"),
    path("create/", CommentCreateView.as_view(), name="comment-create"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "post"
