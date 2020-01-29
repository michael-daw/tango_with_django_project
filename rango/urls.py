from django.urls import path
from rango import views

app name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
]
