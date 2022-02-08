from django.urls import path, include

urlpatterns = [
    path("metar/", include("nws.urls")),
]
