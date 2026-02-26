from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        
        model = User
        fields = ['email','username','password']
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        

class CreateTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        try:
            data =  super().validate(attrs)

            return {
                    "success" : True,
                    "message" : "Login Successful",
                    "data" : {
                        "access" : data['access'],
                        "refresh" : data['refresh'],
                        "user" : {
                            "id" : self.user.id,
                            "email" : self.user.email,
                            "username" : self.user.username
                        }
                    }
                }
        except:
            return {
                    "success" : False,
                    "message" : "Email or password invalid "
                    }