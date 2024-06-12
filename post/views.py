from django.views import generic

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
