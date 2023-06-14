from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import SignupSerializer, LoginSerializer
from rest_framework.views import APIView
from .models import CustomUser

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

# class UserNameView(APIView):
#     def get(self, request, *args, **kwargs):
#         users = CustomUser.objects.all().values_list("username")
#         return Response(
#             data={"users": [u[0] for u in users]}, status=status.HTTP_200_OK
#         )