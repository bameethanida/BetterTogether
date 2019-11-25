from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'BetterTogetherApp/homepage.html')