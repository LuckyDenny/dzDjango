"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

def home_view(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def clients_view(request):
    return render(request, 'clients.html')

def register_view(request):
    return render(request, 'register.html')

def mywork_view(request):
    return render(request, 'mywork.html')

def myprodject_view(request):
    return render(request, 'myprodject.html')

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('clients/', clients_view, name='clients'),
    path('index/', home_view, name='index'),
    path('register/', register_view, name='register'),
    path('mywork/', mywork_view, name='mywork'),
    path('myprodject/', myprodject_view, name='myprodject')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
