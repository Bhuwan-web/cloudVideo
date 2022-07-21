import pathlib
from moviepy.editor import VideoFileClip
from datetime import datetime, timedelta

from utils.price_calc import json_total_pricing


def byte_to_mb(byte) -> float:
    """File size in Mb"""
    unit_mb = 0.000001
    return f"{round(byte * unit_mb, 3)} MB"


def video_extension(video_path) -> str:
    """Extract the extention from the video"""
    return pathlib.Path(video_path).suffix


def video_length(video_path) -> int:
    """return video length in sec"""
    return VideoFileClip(video_path).duration


def get_duration(video_path: str) -> timedelta:
    """return video length in time delata"""
    # return datetime(second=video_length(video_path))
    return timedelta(seconds=video_length(video_path))


def time_to_sec(t):
    h, m, s = map(float, t.split(":"))
    return h * 3600 + m * 60 + s


def perform_price_calculation(data: dict):
    duration: str = data["duration"]
    size: float = float(data["size"])

    sec: int = time_to_sec(duration)
    return json_total_pricing(size, sec)
