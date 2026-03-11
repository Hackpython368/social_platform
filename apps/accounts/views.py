from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,CreateTokenObtainPairSerializer,CreateTokenRefreshPairSerializer,UserViewSerializer
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .models import User
from rest_framework.permissions import AllowAny


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "success" : True,
                "message" : "User registered successfully !",
                "data" : {
                    "id" : user.id,
                    "email" : user.email,
                    "username" : user.username
                }
            }, status=201)

        return Response({
                "success" : False,
                "message" : "Validation failed",
                "error" : serializer.errors
            }, status=400)
    
class CustomTokenObtainPairView(TokenObtainPairView):

    serializer_class = CreateTokenObtainPairSerializer


class CustomTokenRefreshPairView(TokenRefreshView):

    serializer_class = CreateTokenRefreshPairSerializer


class UserView(APIView):


    def get(self,request):

        query = request.GET.get('q')

        if query:
            user = User.objects.filter(username__icontains=query)
        else:
            user = User.objects.all()

        try:
            serializer = UserViewSerializer(user, many=True)
            return Response({
                "success" : True,
                "message" : "The user list is procided in data sections",
                "data" : serializer.data
            },status=200)  
        except:
            return Response({
                "success" : False,
                "message" : "You have to be authinticatied first"
            },status=401)
        

# class UsersearchView(APIView):

#     def get(self, request):

#         user = User.objects.filter(username_icontains= request.GET.get("q"))

#         try:
#             serilaizer = UserViewSerializer(user, many= True)

#             return Response({
#                 "success" : True,
#                 "message" : "The username your are searching is in data field.",
#                 "data" : serilaizer.data
#             },status=200)
#         except:
#             return Response({
#                 "success" : False,
#                 "message" : "some error occurs!!"
#             },status=401)