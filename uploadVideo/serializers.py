from rest_framework import serializers
from uploadVideo.custom_validations import file_length_validation, file_size_validation
from utils.helper_functions import time_to_sec
from utils.price_calc import total_pricing
from . import models


class ReceiveVideoSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name="detail", lookup_field="pk")

    class Meta:
        model = models.ReceiveVideo
        exclude = ("user",)


class VideoDetailsSerializer(serializers.ModelSerializer):
    video = ReceiveVideoSerializer()
    price = serializers.SerializerMethodField()

    def get_price(self, obj) -> str:
        size: float = float(obj.size.split(" ")[0])
        duration: float = time_to_sec(str(obj.duration))
        return f"$ {total_pricing(size, duration)}"

    class Meta:
        model = models.VideoDetails
        fields = "__all__"


class CalcSer(serializers.Serializer):

    duration = serializers.DurationField(validators=[file_length_validation])  # in timedelta
    type = serializers.CharField(max_length=20)
    size = serializers.CharField(max_length=120, validators=[file_size_validation])
