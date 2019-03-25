from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('playerform.html/',views.registerPlayer, name='registerPlayer')
]