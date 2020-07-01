from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<id_poll>', views.detail),
    path('<id_poll>/vote', views.vote),
    path('<id_poll>/results', views.results),
]