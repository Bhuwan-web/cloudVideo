from django.urls import path
from rest_framework.routers import DefaultRouter

from uploadVideo import views

router = DefaultRouter()
router.register(r"videos", views.ReceiveVideoViews, basename="videos")

urlpatterns = [
    # videos/
    path("details/", views.VideoDetailViews.as_view())
]
urlpatterns += router.urls
