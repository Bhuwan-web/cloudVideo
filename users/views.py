from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import generics, mixins, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import CreateUserSerializer, LoginUserSerializer, UserSerializer
from .models import User
from rest_framework_simplejwt.tokens import AccessToken


# View for creating user
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


# View for getting an access token
class LoginUserView(APIView):
    serializer_class = LoginUserSerializer

    # def get(self, request):
    #     return Response(
    #         {
    #             "error": [
    #                 "Get Requset not available for login User",
    #                 "If redirecred from other api's make sure the user is properly logged in",
    #             ]
    #         }
    #     )

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = authenticate(**serializer.validated_data)
            if not user:
                return Response({"error": "wrong credentials"}, status=400)
            access_token = AccessToken.for_user(user)
            return Response({"access_token": str(access_token)})
        return Response({"error": "wrong credentials"}, status=400)


# get current authenticated user
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
