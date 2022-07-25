from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'addpage'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]


def index(request):
    posts = Counter_strike.objects.all()
    return render(request, 'cns/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return HttpResponse("<h1>about</h1>")


def addpage(request):
    return HttpResponse("<h1>addpage</h1>")


def contact(request):
    return HttpResponse("<h1>contact</h1>")


def login(request):
    return HttpResponse("<h1>login</h1>")


def astralis(request):
    return render(request, 'cns/astralis.html', {'menu': menu, 'title': 'Astralis'})

    
def categories(request, csid):
    if int(csid) > 2000:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{csid}</p>")


def show_post(request, post_id):
    return HttpResponse(f"<h1>Отображение статьи</h1><p>{post_id}</p>")


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
