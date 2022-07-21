from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import generics, mixins, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import CreateUserSerializer, LoginUserSerializer, UserSerializer
from .models import User
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework import status

# View for creating user
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = []
    authentication_classes = []


# View for getting an access token
class LoginUserView(APIView):
    serializer_class = LoginUserSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = authenticate(**serializer.validated_data)
            if not user:
                return Response({"error": "wrong credentials"}, status=400)
            access_token = AccessToken.for_user(user)
            refresh_token = RefreshToken.for_user(user)
            return Response(
                {"access_token": str(access_token), "refresh_token": str(refresh_token)},
                status=status.HTTP_200_OK,
            )
        return Response({"error": "wrong credentials"}, status=status.HTTP_406_NOT_ACCEPTABLE)


# get current authenticated user
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
