from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'BetterTogetherApp/homepage.html')

def signup_login(request):
    return render(request, 'BetterTogetherApp/login.html')

def profile(request):
    return render(request, 'BetterTogetherApp/profile.html')