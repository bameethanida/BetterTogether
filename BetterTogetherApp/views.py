from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

def index(request):
    return render(request, 'BetterTogetherApp/index.html')

def share_ride_index(request):
    share_ride = ShareRide.objects.all()
    context = {'share_ride' : share_ride}
    return render(request, 'BetterTogetherApp/share_ride_index.html', context)

# def share_food_index(request):
#     share_food = ShareFood.objects.all()
#     context = {'share_food' : share_food}
#     return render(request, 'BetterTogetherApp/index.html', context)

