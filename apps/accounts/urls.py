from django.urls import path
from .views import RegisterView,CustomTokenObtainPairView,CustomTokenRefreshPairView,UserView

print("Hello From the account")

urlpatterns = [
    path('',CustomTokenObtainPairView.as_view(),name="token_view"),
    path('refresh/',CustomTokenRefreshPairView.as_view(),name="refresh_view"),
    path('register/', RegisterView.as_view(), name="register"),
    path('user/',UserView.as_view(),name="user_serach"),

]