from django.conf.urls import url
from django.urls import path
from . import views
from .views import select_trimestre

urlpatterns = [
    url(r'^home/$', select_trimestre),
]
