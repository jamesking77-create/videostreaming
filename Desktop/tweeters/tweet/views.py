from django.http import HttpResponse
from django.shortcuts import render
from models import Post


# Create your views here.
# all your function must always take in a request
# def welcome(request):
#     return HttpResponse("king welcome to django")

def welcome(request):
    tweets = Post.objects.all()
    return render(request, 'home.html', {"tweets": tweets}),


def tweet_details(request, pk):
    tweet = Post.objects.get(pk=pk)
    return render(request, 'tweet-detail.html', {"tweet": tweet})
