from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from blog.models import Post

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_numbers = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.content
    
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.post.pk})
    
    
