from django.views import generic

from post.models import Comment


class CommentListView(generic.ListView):
    model = Comment
