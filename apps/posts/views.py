from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from .serializer import PostSerializer,CommentSerializer,FeedSerializer
from rest_framework.response import Response
from .models import Post,Like
from apps.connections.models import Follow

# Create your views here.
class PostView(APIView):

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

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
        return Response({
            "success" : True,
            "data" : serializer.data
        },status=201)
    

class LikeView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        
        user = request.user
        id = Post.objects.get(id=id)

        try:
            created = Like.add_like(user,id)
        except:
            return Response({
                            "success" : False,
                            "message":"Unable to create a like!"
                             },status=400)
        
        if created:

            # id = Post_id
            id.like_count += 1
            id.save()
            return Response({
                "success" : True,
                "message":"Create the entry in the database"
            },status=201)
        

        # id = Post_id
        id.like_count -= 1
        id.save()
        return Response({
            "success" : True,
            "message":"Deleted entry form the database"
        },status=200)



class CommentView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, id):

        user = request.user

        id = Post.objects.get(id=id)
        print(request.data)
        try :
            serializer = CommentSerializer(data=request.data)
        except:
            return Response({
                "success" : False,
                "message":"can't able to comment to the post"
            },status=400)

        if serializer.is_valid():
            serializer.save(user=user,post=id)

            # id = Post_id
            id.comment_count += 1
            id.save()
            return Response({
                "success" : True,
                "message": "Comment create Successfully",
                "data" : serializer.data
            },status=201)

        return Response({
            "success" : False,
            "message":"Error will validation data",
            "error" : serializer.errors
        },status=400)


class FeedView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        print(user.id)

        following_id = Follow.objects.all().filter(follower=user).values_list('following',flat=True)

        print(following_id.values_list())

        if not following_id:
            posts = Post.objects.order_by('-created_at')
        else:
            posts = Post.objects.order_by('-created_at')
            # posts = Post.objects.filter(user__in=following_id).order_by('-created_at')


        try :
            serializer = FeedSerializer(posts,many=True,context={'request': request})
        except:
            return Response({
                "success" : False,
                "message":"Error will serializing the data"
            },status=400)
        
        # try:
        return Response({

                "success" : True,
                "message" : "Personalized post feed",
                'user_id' : user.id,
                "data": serializer.data
            },status=200)
        # except:
        #     return Response({
        #         "success" : False,
        #         "message":"some error occurs"
        #     },status=400)
    