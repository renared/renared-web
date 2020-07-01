from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Poll, Choice, VoteHash

# Create your views here.

def index(req):
    return render(req, "polls/index.html", {})

def detail(req,id_poll):
    poll = get_object_or_404(Poll,pk=id_poll)
    return render(req, "polls/detail.html", {'poll':poll})

def vote(req,id_poll):
    return HttpResponse(req,"")

def results(req,id_poll):
    return HttpResponse(req,"")