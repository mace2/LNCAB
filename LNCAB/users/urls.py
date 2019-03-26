from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userform.html/',views.registerUser, name='registerUser'),
    path('playerform.html/',views.registerPlayer, name='registerPlayer'),
    path('login.html/',views.user_login, name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout')
]