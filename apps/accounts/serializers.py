from rest_framework import serializers
from .models import User,Profile
from apps.posts.models import Post
from apps.connections.models import Follow
from apps.posts.serializer import PostSerializer
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


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Profile
        fields = ['bio','profile_pic']





class UserProfileViewSerializer(serializers.ModelSerializer):

    bio = serializers.CharField(source='profile.bio',max_length=500,read_only=True)
    profile_pic = serializers.ImageField(source='profile.profile_pic',read_only=True)
    post = serializers.SerializerMethodField()
    follower = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    class Meta:

        model = User
        fields = ['id','username','bio','profile_pic','post','follower','following']

    def get_post(self, obj):

        post = Post.objects.filter(user=obj).order_by('-created_at')
        if not post:
            return {}
        return PostSerializer(post,many=True).data

    def get_follower(self, obj):

        follower = Follow.objects.filter(following=obj).count()

        return follower
    
    def get_following(self, obj):

        following = Follow.objects.filter(follower=obj).count()

        return following