from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the challenges home page!")

# def january(request):
#     return HttpResponse("Hello world")

# def february(request):
#     return HttpResponse("This is february")

# def march(requst):
#     return HttpResponse("This is march")


"""
Dynamic segment to handle all the months
"""
def monthly_challenges(request,month):
    if month== "january":
        challenge_text = "This is january"
    elif month == "february":
        challenge_text = "this is february"
    elif month == "march":
        challenge_text = "this is march"
    else:
        return HttpResponseNotFound("This month is not supported!!")
    return HttpResponse(challenge_text)