from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Shortener


def home(request):
    return render(request=request, template_name='index.html', context={})


def shortener(request, shorten: str):
    try:
        url = Shortener.objects.filter(shortener=shorten).first()
        url.click_count += 1
        url.save()
        return redirect(url.url)
    except:
        return HttpResponse("<h1>404</h1>")
