from django.db.models.signals import post_save
from django.dispatch import receiver
import os
import pathlib
from utils.helper_functions import byte_to_mb, get_duration, video_extension

from .models import ReceiveVideo, VideoDetails


@receiver(post_save, sender=ReceiveVideo)
def video_details_config(sender, instance, created, **kwargs):
    """Configures the video details every time new video isntance is created"""
    if created:
        video_path = instance.video.path
        byte_size = os.path.getsize(video_path)
        details = VideoDetails(video=instance)
        details.size = byte_to_mb(byte_size)
        details.type = video_extension(video_path)
        details.duration = get_duration(video_path)
        details.save()
