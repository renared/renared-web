from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
    return render(req, "polls/index.html", {})

def detail(req,id_poll):
    return HttpResponse(req,"")

def vote(req,id_poll):
    return HttpResponse(req,"")

def results(req,id_poll):
    return HttpResponse(req,"")