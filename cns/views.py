from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

from .forms import *
from .utils import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'addpage'},
        {'title': "Обратная связь", 'url_name': 'contact'}]


def index(request):
    posts = Counter_strike.objects.all()
    return render(request, 'cns/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'cns/about.html', {'menu': menu, 'title': 'О нас'})


def addpage(request):
    return render(request, 'cns/addpage.html', {'menu': menu, 'title': 'Предложить статью'})


def contact(request):
    return render(request, 'cns/contact.html', {'menu': menu, 'title': 'Контакты'})


# def login(request):
#     return render(request, 'cns/login.html', {'menu': menu, 'title': 'Вход'})


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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'cns/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_llist=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'cns/login.html'

    def get_context_data(self,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self) -> str:
        return reverse_lazy('home')
    

def logout_user(request):
    logout(request)
    return redirect('login')