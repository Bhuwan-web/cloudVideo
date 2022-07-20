from rest_framework import serializers
from . import models


class ReceiveVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReceiveVideo
        # fields = "__all__"
        exclude = ("user",)


class VideoDetailsSerializer(serializers.ModelSerializer):
    video = ReceiveVideoSerializer()

    class Meta:
        model = models.VideoDetails
        fields = "__all__"


class CalculatePricingSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.CalculatePricing
        fields = "__all__"
