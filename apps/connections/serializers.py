from rest_framework import serializers
from apps.accounts.models import User
from .models import Follow



class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['id','email']