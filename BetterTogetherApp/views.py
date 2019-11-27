from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django import forms
from datetime import datetime
from django.contrib.auth import logout

myDate = datetime.now()
formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")


def index(request):
    return render(request, 'BetterTogetherApp/homepage.html')

def signup_login(request):
    return render(request, 'BetterTogetherApp/login.html')

@login_required
def logout_user(request):
    logout(request)
    return render(request, 'BetterTogetherApp/homepage.html')

@login_required
def profile(request):
    user = request.user
    info = request.user.info
    context = {'user':user, 'info':info}
    return render(request, 'BetterTogetherApp/profile.html', context)

def user_profile(request, user_id):
    info_obj = get_object_or_404(Info, pk=user_id)
    pass

@login_required
def join_share_ride(request, shareride_id):
    user = request.user.id
    try:
        sr = get_object_or_404(ShareRide, pk=shareride_id)
    except (KeyError, ShareRide.DoesNotExist):
        return render(request, 'BetterTogetherApp/share_ride_index.html1', {'datetime' : formatedDate})
    else:
        sr.participants.add(user)
    context = {'user': user, 'datetime' : formatedDate}
    return render(request, 'BetterTogetherApp/share_ride_index1.html', context)

@login_required
def join_share_promotion(request, sharepromo_id):
    user = request.user.id
    try:
        sr = get_object_or_404(SharePromotion, pk=sharepromo_id)
    except (KeyError, ShareRide.DoesNotExist):
        return render(request, 'BetterTogetherApp/share_promotion_index1.html', {'datetime' : formatedDate})
    else:
        sr.participants.add(user)
    context = {'user': user, 'datetime' : formatedDate}
    return render(request, 'BetterTogetherApp/share_promotion_index1.html', context)

@login_required
def join_share_food(request, sharefood_id):
    user = request.user.id
    try:
        sr = get_object_or_404(ShareFood, pk=sharepromo_id)
    except (KeyError, ShareFood.DoesNotExist):
        return render(request, 'BetterTogetherApp/share_food_index1.html', {'datetime' : formatedDate})
    else:
        sr.participants.add(user)
    context = {'user': user, 'datetime' : formatedDate}
    return render(request, 'BetterTogetherApp/share_food_index1.html', context)


def share_ride_index(request):
    share_ride = ShareRide.objects.all()
    context = {'share_ride' : share_ride, 'datetime' : formatedDate }
    return render(request, 'BetterTogetherApp/share_ride_index.html', context)

def share_promotion_index(request):
    share_promotion = SharePromotion.objects.all()
    context = {'share_promotion' : share_promotion, 'datetime' : formatedDate }
    return render(request, 'BetterTogetherApp/share_promotion_index.html', context)

def share_food_index(request):
    share_food = ShareFood.objects.all()
    context = {'share_food' : share_food, 'datetime' : formatedDate}
    return render(request, 'BetterTogetherApp/share_food_index.html', context)

@login_required
def create_share_food(request):
    form = ShareFoodForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            location_name = form.data.get('location_name')
            location = form.data.get('location')
            description = form.data.get('description')
            date = form.data.get('day')
            time = form.data.get('time')
            num_people = form.data.get('num_people')
            sr = ShareFood(location_name=location_name,location=location,
             description=description, date_time=(str(f"{date} {time}")), num_people=num_people)   
            sr.save()
            return redirect('BetterTogetherApp:share_food_index1')

    context = {'form': form, 'date_time': DateForm}
    return render(request, 'BetterTogetherApp/share_food_create.html', context)

def delete_share_food(request, sharefood_id):
    share = ShareFood.objects.get(pk=sharefood_id)
    share.delete()
    return redirect('BetterTogetherApp:share_food_index1')

@login_required
def create_share_promotion(request):
    form = SharePromotionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            location_name = form.data.get('location_name')
            location = form.data.get('location')
            brand = form.data.get('brand')
            description = form.data.get('description')
            date = form.data.get('day')
            time = form.data.get('time')
            num_people = form.data.get('num_people')
            sp = SharePromotion(location_name=location_name,location=location, brand=brand, 
            description=description, date_time=(str(f"{date} {time}")), num_people=num_people)   
            sp.save()
            return redirect('BetterTogetherApp:share_promotion_index1')

    context = {'form': form, 'date_time': DateForm}
    return render(request, 'BetterTogetherApp/share_promotion_create.html', context)

def delete_share_promotion(request, sharepromo_id):
    share = SharePromotion.objects.get(pk=sharepromo_id)
    share.delete()
    return redirect('BetterTogetherApp:share_promotion_index1')

@login_required
def create_share_ride(request):
    form = ShareRideForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            location_name = form.data.get('location_name')
            location = form.data.get('location')
            destination_name = form.data.get('destination_name')
            destination = form.data.get('destination')
            description = form.data.get('description')
            date = form.data.get('day')
            time = form.data.get('time')
            num_people = form.data.get('num_people')
            sr = ShareRide(location_name=location_name,location=location, destination_name=destination_name,destination=destination,
             description=description, date_time=(str(f"{date} {time}")), num_people=num_people)   
            sr.save()
            return redirect('BetterTogetherApp:share_ride_index1')

    context = {'form': form, 'date_time': DateForm}
    return render(request, 'BetterTogetherApp/share_ride_create.html', context)


def delete_share_ride(request, shareride_id):
    shareride1 = ShareRide.objects.get(pk=shareride_id)
    shareride1.delete()
    return redirect('BetterTogetherApp:share_ride_index1')

