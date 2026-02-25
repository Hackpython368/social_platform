from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializer import PostSerializer,CommentSerializer
from rest_framework.response import Response
from .models import Post,Like

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
            Like.add_like(user,id)
        except:
            return Response({"detail":"Unable to create a post!"},status=400)
        

        return Response({
            "detail":"create a database entry for your like"
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