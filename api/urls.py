from django.urls import path

from .views import (
    ShortenerCreateAPI
)

urlpatterns = [
    path("shortener/", ShortenerCreateAPI.as_view(), name="shortener")
]
