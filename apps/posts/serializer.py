from rest_framework import serializers
from .models import Post,Like,Comment


class PostSerializer(serializers.ModelSerializer):

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
    liked = serializers.SerializerMethodField()
    latest_comment = serializers.SerializerMethodField()
    class Meta:

        model = Post

        fields = ['id','username','profile_pic','content','post_img','like_count','comment_count','liked','latest_comment','created_at']

    def get_liked(self,obj):

        request = self.context.get('request')
    
        if Like.objects.filter(user=request.user,post=obj).exists():
            return True
        else:
            return False
    
    def get_latest_comment(self,obj):
        result = Comment.objects.filter(post=obj).order_by('-created_at').first()
        if result:
            return CommentSerializer(result).data
        else:
            return None
    
