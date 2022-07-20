import pathlib
from moviepy.editor import VideoFileClip
from datetime import timedelta


def byte_to_mb(byte) -> float:
    """File size in Mb"""
    unit_mb = 0.000001
    return byte * unit_mb


def video_extension(video_path) -> str:
    return pathlib.Path(video_path).suffix


def get_duration(video_path: str) -> timedelta:
    time_in_sec = VideoFileClip(video_path).duration
    return timedelta(seconds=time_in_sec)
