from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Comment
from django.shortcuts import get_object_or_404


class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = "comment/create_comment.html"
    model = Comment
    fields = ["content"]
    
    
    def form_valid(self, form):
        post_info = get_object_or_404(Post, id=self.kwargs.get("pk"))
        form.instance.author = self.request.user
        form.instance.post = post_info
        return super().form_valid(form)
    