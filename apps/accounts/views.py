from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,CreateTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User


class RegisterView(APIView):

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
    print("hello form custom token")
    serializer_class = CreateTokenObtainPairSerializer
