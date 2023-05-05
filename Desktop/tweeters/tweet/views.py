from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# all your function must always take in a request
def welcome(request):
    return HttpResponse("king welcome to django")
