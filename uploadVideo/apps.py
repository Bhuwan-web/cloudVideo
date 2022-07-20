from django.apps import AppConfig


class UploadvideoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "uploadVideo"

    def ready(self):
        import uploadVideo.signals
