from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.index, name="index"),
    path('<id_poll>', views.detail, name="detail"),
    path('<id_poll>/vote', views.vote, name="vote"),
    path('<id_poll>/results', views.results, name="results"),
]