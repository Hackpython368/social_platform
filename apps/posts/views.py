from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializer import PostSerializer,CommentSerializer,FeedSerializer
from rest_framework.response import Response
from .models import Post,Like
from apps.connections.models import Follow

# Create your views here.
class PostView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request):

        try: 
            serializer = PostSerializer(data= request.data)
        except ValueError as e:
            return Response({
                "detail":"Can't able to serilaize",
                "error":str(e)
            },status=400)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
        return Response(serializer.data,status=201)
    

class LikeView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        
        user = request.user
        id = Post.objects.get(id=id)

        try:
            created = Like.add_like(user,id)
        except:
            return Response({"detail":"Unable to create a post!"},status=400)
        
        if created:
            return Response({
                "detail":"Create the entry in the database"
            },status=200)
        return Response({
            "detail":"deleted entry form the database "
        },status=200)



class CommentView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, id):

        user = request.user

        id = Post.objects.get(id=id)

        try :
            serializer = CommentSerializer(data= request.data)

        except:
            return Response({
                "detail":"can't able to comment to the post"
            },status=400)
        print(serializer)
        if serializer.is_valid():
            serializer.save(user=user,post=id)
            return Response(serializer.data,status=200)

        return Response({
            "detail":"some error occurs !"
        },status=400)


class FeedView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        following_id = Follow.objects.all().filter(follower=user).values_list('following',flat=True)

        if not following_id:
            posts = Post.objects.order_by('-created_at')
        else:
            posts = Post.objects.filter(user__in=following_id).order_by('-created_at')


        try :
            serializer = FeedSerializer(posts,many=True)
        except:
            return Response({
                "detail":"Can't able serialize your data"
            })
        
        try:
            return Response(
                serializer.data
                ,status=200)
        except:
            return Response({
                'detial':"some error occurs"
            },status=400)
    