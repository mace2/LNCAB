from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player/<pk>', views.PlayerView.as_view()),
    path('player/delete/secure/', views.remove_player),
    path('<int:pk>',views.logged_user,name='logged_user'),
    path('<int:pk>/',views.logged_user,name='logged_user'),
    path('userform.html/',views.registerUser, name='registerUser'),
    path('playerform.html/',views.registerPlayer, name='registerPlayer'),
    path('login.html/',views.user_login, name='login'),
    path('logout/',views.logoutUser, name='logoutUser')
]


