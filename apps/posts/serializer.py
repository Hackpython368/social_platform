from rest_framework import serializers
from .models import Post,Like,Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = ['content','img']


    def create(self, validated_data):

        return Post.objects.create(**validated_data)
    
class CommentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Comment
        fields = ['comment_text']


    

class FeedSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source="user.username", read_only=True)
    profile_pic = serializers.ImageField(source="user.profile.profile_pic",read_only= True)
    class Meta:

        model = Post

        fields = ['id','username','profile_pic','content','post_img','like_count','comment_count']


    
