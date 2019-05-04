from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
]

urlpatterns+=staticfiles_urlpatterns()