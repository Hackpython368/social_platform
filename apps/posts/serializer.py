from rest_framework import serializers
from .models import Post,Like,Comment


class PostSerializer(serializers.ModelSerializer):
    content = serializers.CharField(required=False)

    class Meta:

        model = Post
        fields = ['content','post_img']


    def create(self, validated_data):

        return Post.objects.create(**validated_data)
    
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username",read_only=True)
    class Meta:

        model = Comment
        fields = ['username','comment_text']


    

class FeedSerializer(serializers.ModelSerializer):

    

    username = serializers.CharField(source="user.username", read_only=True)
    profile_pic = serializers.ImageField(source="user.profile.profile_pic",read_only= True)
    is_liked = serializers.BooleanField()
    latest_comment = serializers.CharField(read_only=True)

    
    class Meta:

        model = Post

        fields = ['id','username','profile_pic','content','post_img','like_count','comment_count','is_liked','latest_comment','created_at']
