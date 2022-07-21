from django.urls import path
from rest_framework.routers import DefaultRouter

from uploadVideo import views

router = DefaultRouter()
router.register(r"videos", views.ReceiveVideoViews, basename="videos")

urlpatterns = [
    # videos/
    path("details/", views.VideoDetailViews.as_view()),
    path("details/<int:pk>", views.VideoDetailRetriveView.as_view(), name="detail"),
    path("calculate-price/", views.CalculatePriceView.as_view()),
]
urlpatterns += router.urls
