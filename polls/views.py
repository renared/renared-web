from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Poll, Choice, VoteHash
from django.db import models

# Create your views here.

def index(req):
    polls = Poll.objects.all()
    return render(req, "polls/index.html", {'polls':polls})

def detail(req,id_poll):
    poll = get_object_or_404(Poll,pk=id_poll)
    return render(req, "polls/detail.html", {'poll':poll, 'n_votes':poll.choice_set.count()})

def vote(req,id_poll):
    try:
            poll = Poll.objects.get(pk=id_poll)
    except (KeyError, Poll.DoesNotExist):
        return HttpResponse(req,"poll inexistant")
    
    try:
        VoteHash.objects.get(poll=id_poll, hash=req.POST['hash'])
    except (KeyError, VoteHash.DoesNotExist):
        votehash = VoteHash(poll=poll,hash=req.POST['hash'])
        votehash.save()
        if poll.choice_type=="MULTIPLE":
            user_votes = req.POST.getlist('choice[]')
            for id in user_votes:
                selected_choice = poll.choice_set.get(pk=id)
                selected_choice.votes += 1
                selected_choice.save()
        elif poll.choice_type=="UNIQUE":
            selected_choice = poll.choice_set.get(pk=req.POST['choice'])
            selected_choice.votes += 1
            selected_choice.save()
    return redirect('polls:results',id_poll=id_poll)

def results(req,id_poll):
    poll = get_object_or_404(Poll,pk=id_poll)
    return render(req, "polls/results.html", {'poll':poll, 'n_votes':poll.choice_set.count()})