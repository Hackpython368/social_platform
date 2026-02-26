"""
URL configuration for social_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView




urlpatterns = [
    path('',include('apps.core.urls')),
    path('api/accounts/',include('apps.accounts.urls')),
    path('api/accounts/con/',include('apps.connections.urls')),
    path('api/accounts/con/<int:id>/',include('apps.connections.urls')),
    path("api/accounts/user/",include('apps.posts.urls')),
    path('api/token/',include('apps.accounts.urls'),name='token_obtain_pair'),
    path('admin/', admin.site.urls),
]
