from django.urls import path
from . import views

app_name = 'myprodject'

urlpatterns = [
    path('', views.myprodject_view, name="myprodject"),
]