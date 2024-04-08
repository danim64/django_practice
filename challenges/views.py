from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def monthly_challenge(request, month): 
    challenge_text = None
    if month == "january":
        challenge_text = "eat no meat for a month"
    if month == "febraury":
        challenge_text = "walk everyday"
    return HttpResponse(challenge_text)
