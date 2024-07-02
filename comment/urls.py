from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>", views.CommentCreateView.as_view(), name="create-comment")
]
