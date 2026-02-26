from django.urls import path
from .views import RegisterView,CustomTokenObtainPairView

print("Hello From the account")

urlpatterns = [
    path('',CustomTokenObtainPairView.as_view(),name="token_view"),
    path('register/', RegisterView.as_view(), name="register")
]