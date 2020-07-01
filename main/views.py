from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blank(req):
    return HttpResponse("C'est l'accueil. Voilà voilà.")

def index(req):
    return render(req, "main/index.html", {})