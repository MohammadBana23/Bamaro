from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import SignupSerializer, LoginSerializer , ProfileSerializer , TravelSerializer
from rest_framework.views import APIView
from .models import CustomUser , Travel
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .api import CustomException

class SignUpView(GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class ProfileView(GenericAPIView):
    serializer_class = ProfileSerializer
    def get_queryset(self, username):
        # return the user with the given username
        try:
            if username is None:
                user = CustomUser.objects.get(username=self.request.user.username)
                return user
            else:
                user = CustomUser.objects.get(username=username)
                return user
        except:
            raise CustomException(
                "کاربری با این شناسه وجود ندارد.",
                "error",
                status_code=status.HTTP_404_NOT_FOUND,
            )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'Authorization', 
                openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Bearer Token',
                required=False,
            ),
        ]
    )
    def get(self, request, username=None, *args, **kwargs):
        query = self.get_queryset(username)
        serializer = self.serializer_class(query)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TravelView(GenericAPIView):
    serializer_class = TravelSerializer
    
    def get(self , request):
        queryset = Travel.objects.all()
        serializer = self.serializer_class(queryset , many=True)
        return Response(serializer.data , status = status.HTTP_200_OK)

# class UserNameView(APIView):
#     def get(self, request, *args, **kwargs):
#         users = CustomUser.objects.all().values_list("username")
#         return Response(
#             data={"users": [u[0] for u in users]}, status=status.HTTP_200_OK
#         )