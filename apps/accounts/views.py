from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,CreateTokenObtainPairSerializer,CreateTokenRefreshPairSerializer,UserViewSerializer,ProfileSerializer,UserProfileViewSerializer
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .models import User,Profile
from rest_framework.permissions import AllowAny,IsAuthenticated


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
        
class ProfileUpdate(APIView):

    permission_classes = [IsAuthenticated]
    
    def post(self,request):

        profile = Profile.objects.get(user=request.user)
        
        serializer = ProfileSerializer(profile,data=request.data,partial= True)


        if serializer.is_valid():
            serializer.save()
            return Response({
                'success' : True,
                'data' : serializer.data
            },status=201)
        return Response({
            'success' : False,
            'error' : serializer.errors
        },status=400)
        
class UserprofileView(APIView):
    

    def get(self,request, id):
        user = User.objects.get(id=id)

        try:
            serializer = UserProfileViewSerializer(user)
            return Response({
                'success' : True,
                'data' : serializer.data
            },status=200)
        except:
            return Response({
                "success" : False,
                "message" : "Some error occurs while serializing data"
            },status=200)