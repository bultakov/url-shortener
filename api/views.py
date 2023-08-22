from rest_framework.generics import CreateAPIView

from shortener.models import Shortener
from .serializers import ShortenerCreateSerializer


class ShortenerCreateAPI(CreateAPIView):
    model = Shortener
    serializer_class = ShortenerCreateSerializer
