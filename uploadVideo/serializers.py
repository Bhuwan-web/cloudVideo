from rest_framework import serializers
from uploadVideo.custom_validations import file_length_validation, file_size_validation
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


# class CalculatePricingSerialiser(serializers.ModelSerializer):
#     class Meta:
#         model = models.CalculatePricing
#         fields = "__all__"


class CalcSer(serializers.Serializer):

    duration = serializers.DurationField(validators=[file_length_validation])  # in timedelta
    type = serializers.CharField(max_length=20)
    size = serializers.CharField(max_length=120, validators=[file_size_validation])
