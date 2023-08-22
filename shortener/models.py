from django.db import models


class Shortener(models.Model):
    url = models.CharField(max_length=255)
    shortener = models.CharField(max_length=255)
    click_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='qrcode/')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url} -> {self.shortener}"
