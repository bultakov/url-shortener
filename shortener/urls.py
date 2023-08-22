from django.urls import path

from .views import (
    home,
    shortener
)

urlpatterns = [
    path("", home, name="home"),
    path("<str:shorten>/", shortener, name="shortener"),
]
