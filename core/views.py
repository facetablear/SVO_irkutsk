from django.http import HttpResponse
from django.shortcuts import render

from .models import News


def home(request):
    news = News.objects.all()
    _context = {'news': news,
                'title': 'Домашняя страница', }
    return render(request, 'core/home.html', _context)
