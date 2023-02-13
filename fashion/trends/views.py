from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

def index(request):
    posts = Trends.objects.all()
    return render(request, 'trends/index.html', {'posts': posts},)

def about(request):
    return render(request, 'trends/about.html',{'title': 'О сайте'})

def categ(request, categ):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Cписок статей</h1><p>{categ}</p>')

def archive(request, year):
    if int(year) > 2023:
        #raise Http404()
        return redirect('home', permanent=True,)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exсeption):
    return HttpResponseNotFound('Страница не найдена')

# Create your views here.
