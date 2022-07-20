from datetime import timedelta
from django.core.exceptions import ValidationError
from utils.helper_functions import video_length
from utils.helper_functions import time_to_sec


def file_size_validation(value):
    """
    Validate the file size to be less than a GB.
    """
    if isinstance(value, str):
        if not float(value) > 1024:  # 1gb =1024 mb
            return
    else:
        if not value.size > 10**9:  # 1 gb =10^9 bytes
            return
    raise ValidationError("File size cannot exceed more than 1GB")


def file_length_validation(value):

    MAX_LENGTH = 10 * 60  # 10 minute

    if isinstance(value, timedelta):
        vid_len = time_to_sec(str(value))
        if vid_len <= MAX_LENGTH:
            return
    else:
        try:
            video_path = value.file.name
        except AttributeError:
            raise ValidationError("Cannot process video file path")

        vid_len = video_length(video_path)
        if vid_len < MAX_LENGTH:
            return

    raise ValidationError("Video cannot exceed 10 minutes in length")
