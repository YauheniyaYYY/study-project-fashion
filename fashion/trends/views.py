from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request,'trends/addpage.html',{"menu": menu, 'title':"Добавить статью"})
def contact(request):
    return HttpResponse("Обратная связь")

def showpost(request, post_slug):
    post = get_object_or_404(Trends, slug = post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'trends/post.html', context=context)
def show_category(request, cat_id):
    posts = Trends.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    context={
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    if len(posts) == 0:
        raise Http404()
    return render(request, 'trends/index.html',context=context)


