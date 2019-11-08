from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django import forms

def index(request):
    return render(request, 'BetterTogetherApp/index.html')

def share_ride_index(request):
    share_ride = ShareRide.objects.all()
    dateform = DateForm
    context = {'share_ride' : share_ride,
                'dateform' : dateform}
    return render(request, 'BetterTogetherApp/share_ride_index.html', context)

# def share_food_index(request):
#     share_food = ShareFood.objects.all()
#     context = {'share_food' : share_food}
#     return render(request, 'BetterTogetherApp/index.html', context)

# def share_promotion_index(request):
#     share_promotion = SharePromotion.objects.all()
#     context = {'share_promotion' : share_promotion}
#     return render(request, 'BetterTogetherApp/index.html', context)

def user_profile(request, user_id):
    pass

def create_share_food(request):
    pass


def create_share_promotion(request):
    pass

def create_share_ride(request):
    form = ShareRideForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            location = form.data.get('location')
            destination = form.data.get('destination')
            description = form.data.get('description')
            date_time = form.data.get('date_time')
            num_people = form.data.get('num_people')
            sr = ShareRide(location=location, destination=destination,
             description=description, date_time=date_time, num_people=num_people)   
            sr.save()
            return redirect('BetterTogetherApp:share_ride_index1')

    context = {'form': form}
    return render(request, 'BetterTogetherApp/share_ride_create.html', context)