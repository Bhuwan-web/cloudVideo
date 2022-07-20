from django.shortcuts import redirect
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from uploadVideo import serializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import AnonymousUser
from rest_framework.response import Response
from .permissions import IsOwner
from . import models

# Create your views here.


class ReceiveVideoViews(ModelViewSet):
    queryset = models.ReceiveVideo.objects.all()
    serializer_class = serializers.ReceiveVideoSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        self.queryset = models.ReceiveVideo.objects.filter(user=self.request.user)
        return super().get_queryset()


class VideoDetailViews(ListAPIView):
    serializer_class = serializers.VideoDetailsSerializer
    # queryset = models.VideoDetails.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        current_user = self.request.user

        self.queryset = models.VideoDetails.objects.filter(video__user=current_user)
        return super().get_queryset()
