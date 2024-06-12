from django.urls import reverse_lazy
from django.views import generic

from post.forms import CommentForm
from post.models import Comment


class CommentListView(generic.ListView):
    model = Comment
    paginate_by = 25

    def get_queryset(self):
        queryset = super().get_queryset().filter(parent__isnull=True)
        sort_field = self.request.GET.get('sort', 'created_at')
        sort_order = self.request.GET.get('order', 'desc')

        if sort_field and sort_order:
            if sort_order == 'asc':
                queryset = queryset.order_by(sort_field)
            elif sort_order == 'desc':
                queryset = queryset.order_by(f'-{sort_field}')

        return queryset


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy("comment-list")

    def form_valid(self, form):
        parent_id = self.request.POST.get("parent_id")
        if parent_id:
            parent_comment = Comment.objects.get(id=parent_id)
            form.instance.parent = parent_comment
        return super().form_valid(form)
