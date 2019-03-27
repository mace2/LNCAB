from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userform.html/',views.reigsterUser, name='registerUser'),
    path('playerform.html/',views.registerPlayer, name='registerPlayer')
]
