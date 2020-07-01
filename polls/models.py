from django.db import models
from django.utils import timezone

class Poll(models.Model):
    question_text = models.CharField(max_length=300)
    #author = models.CharField(max_length=42)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    choice_type = models.CharField(max_length=12, verbose_name="Type de choix. 'UNIQUE' pour des ptits ronds, 'MULTIPLE' pour des carrés, 'POURCENT' pour des pourcentages")

    class Meta:
        verbose_name = "Sondage"
        ordering =  ["date"]

class Choice(models.Model):
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.FloatField(default=0)

    class Meta:
        verbose_name = "Choix"

class VoteHash(models.Model):
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    hash = models.SlugField(max_length=32)

    class Meta:
        verbose_name = "Choix"
        ordering = ["poll"]
