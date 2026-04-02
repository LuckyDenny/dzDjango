from django.urls import path
from . import views

app_name = 'mywork'

urlpatterns = [
    path('', views.mywork_view, name="mywork"),
]