from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import TeamView

from . import views

urlpatterns = [
    path('<pk>', TeamView.as_view())
]

urlpatterns+=staticfiles_urlpatterns()