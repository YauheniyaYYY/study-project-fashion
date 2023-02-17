from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [{ "title": "О нас", 'url_name': 'about'},
        { "title": "Добавить статью", 'url_name': 'add_page'},
        {"title": "Обратная связь", 'url_name': 'contact'} ]
def index(request):
    posts = Trends.objects.all()
    cats = Category.objects.all()
    context={
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,

    }
    return render(request, 'trends/index.html',context=context)

def about(request):
    return render(request, 'trends/about.html',{'menu': menu, 'title': 'О сайте'})
def addpage(request):
    return HttpResponse("Добавить статью")
def contact(request):
    return HttpResponse("Обратная связь")

def showpost(request, post_id):
    return HttpResponse(f"Отображение статьи c id={post_id}")
def show_category(request, cat_id):
    posts = Trends.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
def show_category(request, cat_id):
    return HttpResponse(f"Отображение статьи c id={cat_id}")

def archive(request, year):
    if int(year) > 2023:
        #raise Http404()
        return redirect('home', permanent=True,)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exсeption):
    return HttpResponseNotFound('Страница не найдена')

# Create your views here.
