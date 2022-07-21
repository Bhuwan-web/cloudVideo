from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from crum import get_current_user


from django.utils import timezone

from uploadVideo.custom_validations import file_length_validation, file_size_validation


class ReceiveVideoManger(models.Manager):
    """
    Custom manager to filter queryset directly from manager

    filter the user as the current user and the post which are scheduled before current date and time
    """

    def get_queryset(self):
        current_user = get_current_user()
        now = timezone.now()
        return super().get_queryset().filter(user=current_user, uploaded_at__lte=now)


class VideoDetailManager(models.Manager):
    """
    Flitered data from manager

    this manager filters out the data of vodeo details with respect to the properties from Receive Video database properties
    """

    def get_queryset(self):
        now = timezone.now()
        current_user = get_current_user()
        return super().get_queryset().filter(video__user=current_user, video__uploaded_at__lte=now)


# Create your models here.
class ReceiveVideo(models.Model):
    """Get basic video details"""

    caption = models.CharField(max_length=150)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=get_current_user
    )
    video = models.FileField(
        upload_to="video/",
        validators=[
            FileExtensionValidator(["mp4", "mkv"], "Try Uploading 'mp4' or 'mkv' files"),
            file_size_validation,
            file_length_validation,
        ],
    )
    uploaded_at = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    user_obj = ReceiveVideoManger()

    def __str__(self):
        return self.caption


class VideoDetails(models.Model):
    """
    Generate video details and save

    use signals to use the instance of ReceiveVideo model when created and use it's info to make video necessary details and save
    """

    video = models.ForeignKey(ReceiveVideo, on_delete=models.CASCADE)
    duration = models.DurationField(null=True)  # in timedelta
    type = models.CharField(max_length=20, null=True)
    size = models.CharField(null=True, max_length=120)

    objects = models.Manager()
    user_obj = VideoDetailManager()

    def __str__(self) -> str:
        return f"{self.video.caption} Details"


# class CalculatePricing(models.Model):
#     """
#     Pricing model to calculate the price policy

#     it is just made to make UI based more
#     """

#     duration = models.DurationField(null=True, validators=[file_length_validation])  # in timedelta
#     type = models.CharField(max_length=20, null=True)
#     size = models.CharField(null=True, max_length=120, validators=[file_size_validation])
