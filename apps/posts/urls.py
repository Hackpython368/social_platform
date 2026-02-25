from django.urls import path
from .views import PostView,LikeView,CommentView,FeedView


urlpatterns = [
    path('create/post/',PostView.as_view()),
    path('<int:id>/post/like/',LikeView.as_view()),
    path('<int:id>/post/comment/',CommentView.as_view()),
    path('feed/',FeedView.as_view())
]