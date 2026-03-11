from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer


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
        
        

class CreateTokenRefreshPairSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        try:
            data =  super().validate(attrs)

            return {
                    "success" : True,
                    "message" : "Login Successful",
                    "data" : {
                        "access" : data['access'],
                    }
                }
        except:
            return {
                    "success" : False,
                    "message" : "Email or password invalid "
                    }
        
class UserViewSerializer(serializers.ModelSerializer):

    bio = serializers.CharField(source="profile.bio",max_length=500,read_only= True)
    profile_pic = serializers.ImageField(source="profile.profile_pic",read_only=True)

    class Meta:

        model = User
        fields = ['id','username','bio','profile_pic']