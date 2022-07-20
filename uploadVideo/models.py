from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from crum import get_current_user

# Create your models here.
class ReceiveVideo(models.Model):
    """Get basic video details"""

    caption = models.CharField(max_length=150)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=get_current_user
    )
    video = models.FileField(upload_to="video/%y", validators=[FileExtensionValidator(["mp4", "mkv"])])

    def __str__(self):
        return self.caption


class VideoDetails(models.Model):
    """
    Generate video details and save

    use signals to use the instance of ReceiveVideo model when created and use it's info to make video necessary detaials and save
    """

    video = models.ForeignKey(ReceiveVideo, on_delete=models.CASCADE)
    duration = models.DurationField(null=True)  # in timedelta
    type = models.CharField(max_length=20, null=True)
    size = models.FloatField(null=True)

    def __str__(self) -> str:
        return f"{self.video.caption} Details"
