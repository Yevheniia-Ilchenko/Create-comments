from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from post.forms import CommentForm
from post.models import Comment


class CommentListView(generic.ListView):
    model = Comment
    paginate_by = 25

    def get_queryset(self):
        queryset = super().get_queryset().filter(parent__isnull=True)
        sort_field = self.request.GET.get("sort", "created_at")
        sort_order = self.request.GET.get("order", "desc")

        if sort_field and sort_order:
            if sort_order == "asc":
                queryset = queryset.order_by(sort_field)
            elif sort_order == "desc":
                queryset = queryset.order_by(f"-{sort_field}")

        return queryset


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy("post:comment-list")

    def form_valid(self, form):
        parent_id = self.request.POST.get("parent_id")
        if parent_id:
            parent_comment = Comment.objects.get(id=parent_id)
            form.instance.parent = parent_comment
        return super().form_valid(form)


def add_comment(request, parent_comment_id=None):
    parent_comment = None
    if parent_comment_id:
        parent_comment = get_object_or_404(Comment, id=parent_comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.parent = parent_comment
            comment.save()
            return redirect(reverse('post:comment-list'))
    else:
        form = CommentForm()

    return render(request, 'comment_form.html', {'form': form})
