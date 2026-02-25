from django.urls import path
from .views import FollowerView


urlpatterns = [
    
    path('follow/',FollowerView.as_view(), name="follow"),
    path('<str:name>/count/',FollowerView.as_view(),name="follower_count"),
    path('<str:name>/count/',FollowerView.as_view(),name="following_count"),
]