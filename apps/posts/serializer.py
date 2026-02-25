from rest_framework import serializers
from .models import Post,Like,Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = ['content']


    def create(self, validated_data):

        return Post.objects.create(**validated_data)
    
class CommentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Comment
        fields = ['user','post','comment_text']


    