from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Follow
from .serializers import UserSerializer
from apps.accounts.models import User



# Create your views here.
class FollowerView(APIView):

    permission_classes = [IsAuthenticated]
    

    def post(self, request, id):

        follower = request.user
        try:
            following = User.objects.get(id=id)
        except:
            return Response({
                "success" : False,
                "message":"User is not Found 404"
            },status=404)
        

        try :
            follow , created = Follow.user_follower(follower,following)
        except ValueError:
            return Response({
                "success" : False,
                "message":"User can't follow himself !"
            },status=400)
        
        if created:
            return Response({
                "success" : True,
                "message" : f"{follower} is following {following}"
            },status=200)
        
        return Response({
            "success" : True,
            "message":f"{follower} Aready follow {following}"
            },status=200)

    def delete(self, request, id):

        follower = request.user

        try:
            following = User.objects.get(id=id)
        except:
            return Response({
                "success" : False,
                "message":"Invalid User"
            },status=404)
        try:
            unfollow = Follow.user_unfollow(follower,following)
        except ValueError as e:
            return Response({

                "success" : False,
                "message": str(e)
            },status=400)

        if not unfollow:
            return Response({
                "success" : True,
                "message": "You are not following this user"
            },status=400)

        return Response({"success" : True,"message": "Unfollowed successfully"},status=204)


    def get(self, request, name):

        if name=="follower":
            try:
                follower = Follow.objects.filter(following=request.user)
                user = [i.follower for i in follower]
                serializer = UserSerializer(user,many=True)
            except ValueError as e:
                return Response({
                    "success" :False,
                    "message":"User you are enter is invalid or unavilable",
                    "error" : str(e)
                    },status=404)
            
            return Response({
                    "success" : True,
                    "message" : "follower count",
                    "data": {

                        "count":follower.count(),
                        "list":serializer.data
                    }
                },status=200)
        
        elif name=="following":
            try:
                following = Follow.objects.filter(follower=request.user)
                user = [i.following for i in following]
                print(user)
                serializer = UserSerializer(user,many=True)

            except ValueError as e:
                return Response({
                        "success" : False,
                        "message":"User you are enter is invalid or unavilable",
                        "error" : str(e)
                        },status=404)
            
            return Response({
                        "success" : True,
                        "message" : "follower count",
                        "data": {

                            "count":following.count(),
                            "list":serializer.data
                        }
                    },status=200)
        else:
            return Response({
                "success" : False,
                "message" : "The url you are trying get is invalid kindly url",
                "url" : {
                    "1" : "api/accounts/con/follower/count/",
                    "2" : "api/accounts/con/following/count/"
                }
            },status=404)