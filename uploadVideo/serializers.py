from rest_framework import serializers
from . import models


class ReceiveVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReceiveVideo
        fields = "__all__"


class VideoDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VideoDetails
        fields = "__all__"
