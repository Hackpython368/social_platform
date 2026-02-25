from django.urls import path
from .views import RegisterView

print("Hello From the account")

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
]