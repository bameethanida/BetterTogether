from django.shortcuts import render, reverse, get_object_or_404, redirect, reverse
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
    if request.user.is_authenticated:
        return redirect('BetterTogetherApp:index')
    else:
        return render(request, 'BetterTogetherApp/login.html')


@login_required
def logout_user(request):
    print(request.user)
    logout(request)
    print(request.user)
    return redirect(reverse('BetterTogetherApp:index'))

@login_required
def profile(request):
    user = request.user
    info = request.user.info
    print(request.user)
    context = {'user':user, 'info':info}
    return render(request, 'BetterTogetherApp/profile.html', context)

@login_required
def edit_profile(request):
    form = EditInfo(request.POST or None)
    info = request.user.info
    if request.method == 'POST':
        if form.is_valid():
            gender = form.data.get('gender')
            birthday = form.data.get('birthday')
            brief_info = form.data.get('brief_info')
            phone_num = form.data.get('phone_num')
            twitter = form.data.get('twitter')
            info.gender = gender
            info.save()
            info.birthday = birthday
            info.save()
            info.brief_info = brief_info
            info.save()
            info.phone_num = phone_num
            info.save()
            info.twitter = twitter
            info.save()
            return redirect('BetterTogetherApp:profile')
    
    context = {'form': form, 'date_time': DateForm, 'info' : info}
    return render(request, 'BetterTogetherApp/edit_profile.html', context)

def user_profile(request, user_id):
    info_obj = get_object_or_404(Info, pk=user_id)
    pass

@login_required
def join_share_ride(request, shareride_id):
    user = request.user.id
    try:
        sr = get_object_or_404(ShareRide, pk=shareride_id)
    except (KeyError, ShareRide.DoesNotExist):
        return render(request, 'BetterTogetherApp/share_ride_index.html', {'datetime' : formatedDate})
    else:
        sr.participants.add(user)
    return redirect('BetterTogetherApp:share_ride_index1')

@login_required
def leave_share_ride(request, shareride_id):
    user = request.user.id
    try:
        sr = get_object_or_404(ShareRide, pk=shareride_id)
    except (KeyError, ShareRide.DoesNotExist):
        return render(request, 'BetterTogetherApp/share_ride_index.html', {'datetime' : formatedDate})
    else:
        sr.participants.remove(user)
    return redirect('BetterTogetherApp:share_ride_index1')

@login_required
def join_share_promotion(request, sharepromo_id):
    user = request.user.id
    try:
        sr = get_object_or_404(SharePromotion, pk=sharepromo_id)
    except (KeyError, ShareRide.DoesNotExist):
        return render(request, 'BetterTogetherApp/share_promotion_index.html', {'datetime' : formatedDate})
    else:
        sr.participants.add(user)
    return redirect('BetterTogetherApp:share_promotion_index1')

@login_required
def join_share_food(request, sharefood_id):
    user = request.user.id
    try:
        sr = get_object_or_404(ShareFood, pk=sharefood_id)
    except (KeyError, ShareFood.DoesNotExist):
        return render(request, 'BetterTogetherApp/share_food_index.html', {'datetime' : formatedDate})
    else:
        sr.participants.add(user)
    return redirect('BetterTogetherApp:share_food_index1')


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
             description=description, date_time=(str(f"{date} {time}")), num_people=num_people, host=request.user.info.get_name(), 
             host_gender=request.user.info.get_gender())
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
            description=description, date_time=(str(f"{date} {time}")), num_people=num_people, host=request.user.info.get_name(), 
             host_gender=request.user.info.get_gender())   
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
             description=description, date_time=(str(f"{date} {time}")), num_people=num_people, host=request.user.info.get_name(), 
             host_gender=request.user.info.get_gender())   
            sr.save()
            return redirect('BetterTogetherApp:share_ride_index1')

    context = {'form': form, 'date_time': DateForm}
    return render(request, 'BetterTogetherApp/share_ride_create.html', context)


def delete_share_ride(request, shareride_id):
    shareride1 = ShareRide.objects.get(pk=shareride_id)
    shareride1.delete()
    return redirect('BetterTogetherApp:share_ride_index1')

