"""
API-level router
"""
from django.urls import path
from .views import ClientAPIView, StatusAPIView

urlpatterns = [
    path("info", ClientAPIView.as_view(), name="weather_info"),
    path("ping", StatusAPIView.as_view(), name="status"),
]
