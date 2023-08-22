from django.shortcuts import render, redirect

from .models import Shortener


def home(request):
    return render(request=request, template_name='index.html', context={})


def shortener(request, shorten: str):
    url = Shortener.objects.filter(shortener=shorten).first()
    url.click_count += 1
    url.save()
    return redirect(url.url)
