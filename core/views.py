from django.shortcuts import render
from django.shortcuts import HttpResponse

from . import models


def index(request):
    news = models.News.objects.all()
    return render(request, 'core/index.html', {'news': news, 'title': 'Список новостей'})
