import re

from django.core.files.images import ImageFile
from rest_framework.serializers import ModelSerializer, RegexField, URLField, CharField

from .utils import hashed_url, generate_qrcode
from shortener.models import Shortener


class ShortenerCreateSerializer(ModelSerializer):
    url = URLField()
    host = CharField(min_length=5, max_length=255)

    class Meta:
        model = Shortener
        fields = [
            'url',
            'host'
        ]

    def create(self, validated_data):
        shortener = hashed_url(url=validated_data.get('url'))
        qr = generate_qrcode(url=f"{validated_data.get('host')}/{shortener}")
        instance = Shortener.objects.create(
            url=validated_data.get('url'),
            shortener=shortener,
            image=ImageFile(qr, name=f'{shortener}.png')
        )
        return instance

    def to_representation(self, instance):
        return ShortenerSerializer(instance).data


class ShortenerSerializer(ModelSerializer):
    class Meta:
        model = Shortener
        fields = [
            'url',
            'shortener',
            'image',
        ]
