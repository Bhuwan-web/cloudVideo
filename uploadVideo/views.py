from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from uploadVideo import serializers
from rest_framework.permissions import IsAuthenticated

from utils.helper_functions import perform_price_calculation
from .permissions import IsOwner
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ReceiveVideoViews(ModelViewSet):
    queryset = models.ReceiveVideo.objects.all()
    serializer_class = serializers.ReceiveVideoSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filterset_fields = {"uploaded_at": ["gte", "lte"]}
    ordering_fields = "__all__"
    ordering = [
        "-uploaded_at",
    ]

    def get_queryset(self):
        self.queryset = models.ReceiveVideo.user_obj.all()
        return super().get_queryset()


class VideoDetailViews(ListAPIView):
    serializer_class = serializers.VideoDetailsSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filterset_fields = {"duration": ["gte", "lte"], "size": ["gte", "lte"]}

    def get_queryset(self):
        self.queryset = models.VideoDetails.user_obj.all()
        return super().get_queryset()


class VideoDetailRetriveView(RetrieveAPIView, VideoDetailViews):
    """Inheritated properties get't the job done"""

    pass


class CalculatePriceView(CreateAPIView):
    serializer_class = serializers.CalcSer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        json_total_price = perform_price_calculation(data)
        headers = self.get_success_headers(serializer.data)
        return Response({**data, **json_total_price}, status=status.HTTP_200_OK, headers=headers)
