from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Shortener

admin.site.register(
    [
        Shortener
    ]
)

admin.site.unregister(User)
admin.site.unregister(Group)