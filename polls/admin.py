from django.contrib import admin
from .models import Poll, Choice, VoteHash

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(VoteHash)