from django.shortcuts import render
from django.http import Http404

from .models import StaticPage

def index(request, slug):
    try:
        staticpage = StaticPage.objects.get(url=slug)
    except StaticPage.DoesNotExist:
        raise Http404("Page does not exist")

    return render(request, "staticpages/index.html", {'staticpage': staticpage})
