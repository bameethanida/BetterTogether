from django.shortcuts import render, reverse, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django import forms
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

myDate = datetime.now()
formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")


def index(request):
    """Render homepage's page"""
    return render(request, 'BetterTogetherApp/homepage.html')

def all_share(request):
    """Collection of all shares (share food, ride, promotion)"""
    sr = ShareRide.objects.all()
    sf = ShareFood.objects.all()
    sp = SharePromotion.objects.all()
    user = request.user
    context = {'user':user, 'sr':sr, 'sf':sf, 'sp':sp}
    return render(request, 'BetterTogetherApp/all_share.html', context)

def login_user(request, backend='django.contrib.auth.backends.ModelBackend'):
    """If the user is not authenticated, get user's request and execute login."""
    if not request.user.is_authenticated:
        form2 = SignIn(request.POST)
        if request.method == "POST":
            username = form2.data.get('username')
            password = form2.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('BetterTogetherApp:index'))
                # redirect('/login/next=%s' %request.path)
            else:
                message = "Attention: Wrong Username or Password"
                return render(request, 'BetterTogetherApp/login.html', {'form2': form2, 'message': message})
        else:
            return render(request, 'BetterTogetherApp/login.html', {'form2': form2})

    return HttpResponseRedirect(reverse('BetterTogetherApp:index'))

def signup(request):
    """Get user's infomation, create user account and save to database. Also, allowing user to join and create event"""
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.data.get('username')
            raw_password = form.data.get('password1')
            first_name = form.data.get('first_name')
            last_name = form.data.get('last_name')
            user = authenticate(username=username, password=raw_password, first_name=first_name, last_name=last_name)
            login(request, user)
            return HttpResponseRedirect(reverse('BetterTogetherApp:index'))
        else:
            message = form.errors.as_data()
            for value in message:
                form = message[value][0]
                message = str(form).strip('[]')
                print(message)
            form = SignUp()
            return render(request, 'BetterTogetherApp/signup.html', {'form': form, 'message': message})
    else:
        form = SignUp() 
    return render(request, 'BetterTogetherApp/signup.html', {'form': form})


@login_required
def logout_user(request):
    """Logout mode"""
    print(request.user)
    logout(request)
    return redirect(reverse('BetterTogetherApp:index'))

@login_required
def profile(request):
    """User's profile"""
    user = request.user
    info = request.user.info
    context = {'user':user, 'info':info}
    return render(request, 'BetterTogetherApp/profile.html', context)

@login_required
def edit_profile(request):
    """Users can edit their profile"""
    form = EditInfo(request.POST or None)
    info = request.user.info
    if request.method == 'POST':
        if form.is_valid():
            gender = form.data.get('gender')
            birthday = form.cleaned_data.get('birthday')
            brief_info = form.data.get('brief_info')
            phone_num = form.data.get('phone_num')
            twitter = form.data.get('twitter')
            print(f"Birthday: {form.data.get('birthday')}")
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

@login_required
def join_share_ride(request, shareride_id):
    """User can join share ride event with their account"""
    user = request.user.id
    try:
        sr = get_object_or_404(ShareRide, pk=shareride_id)
    except (KeyError, ShareRide.DoesNotExist):
        return redirect('BetterTogetherApp:share_ride_index1')
    else:
        sr.participants.add(user)
    return redirect('BetterTogetherApp:share_ride_index1')

@login_required
def leave_share_ride(request, shareride_id):
    """User can leave share ride event"""
    user = request.user.id
    try:
        sr = get_object_or_404(ShareRide, pk=shareride_id)
    except (KeyError, ShareRide.DoesNotExist):
        return redirect('BetterTogetherApp:share_ride_index1')
    else:
        sr.participants.remove(user)
    return redirect('BetterTogetherApp:share_ride_index1')

@login_required
def join_share_promotion(request, sharepromo_id):
    """User can join share promotion event with their account"""
    user = request.user.id
    try:
        sp = get_object_or_404(SharePromotion, pk=sharepromo_id)
    except (KeyError, ShareRide.DoesNotExist):
        return redirect('BetterTogetherApp:share_promotion_index1')
    else:
        sp.participants.add(user)
    return redirect('BetterTogetherApp:share_promotion_index1')

@login_required
def leave_share_promo(request, sharepromo_id):
    """User can leave share promotion event"""
    user = request.user.id
    try:
        sp = get_object_or_404(SharePromotion, pk=sharepromo_id)
    except (KeyError, SharePromotion.DoesNotExist):
        return redirect('BetterTogetherApp:share_promotion_index1')
    else:
        sp.participants.remove(user)
    return redirect('BetterTogetherApp:share_promotion_index1')

@login_required
def join_share_food(request, sharefood_id):
    """User can join share food event with their account"""
    user = request.user.id
    try:
        sf = get_object_or_404(ShareFood, pk=sharefood_id)
    except (KeyError, ShareFood.DoesNotExist):
        return redirect('BetterTogetherApp:share_food_index1')
    else:
        sf.participants.add(user)
    return redirect('BetterTogetherApp:share_food_index1')

@login_required
def leave_share_food(request, sharefood_id):
    """User can leave share food event"""
    user = request.user.id
    try:
        sf = get_object_or_404(ShareFood, pk=sharefood_id)
    except (KeyError, ShareFood.DoesNotExist):
        return redirect('BetterTogetherApp:share_food_index1')
    else:
        sf.participants.remove(user)
    return redirect('BetterTogetherApp:share_food_index1')


def share_ride_index(request):
    """Render share ride's page"""
    share_ride = ShareRide.objects.all()
    context = {'share_ride' : share_ride, 'datetime' : formatedDate }
    return render(request, 'BetterTogetherApp/share_ride_index.html', context)

def share_promotion_index(request):
    """Render share promotion's page"""
    share_promotion = SharePromotion.objects.all()
    context = {'share_promotion' : share_promotion, 'datetime' : formatedDate }
    return render(request, 'BetterTogetherApp/share_promotion_index.html', context)

def share_food_index(request):
    """Render share food's page"""
    share_food = ShareFood.objects.all()
    context = {'share_food' : share_food, 'datetime' : formatedDate}
    return render(request, 'BetterTogetherApp/share_food_index.html', context)

@login_required
def create_share_food(request):
    """User creates share food event"""
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
             host_gender=request.user.info.get_gender(), host_number=request.user.info.get_number())
            sr.save()
            return redirect('BetterTogetherApp:share_food_index1')

    context = {'form': form, 'date_time': DateForm}
    return render(request, 'BetterTogetherApp/share_food_create.html', context)

def delete_share_food(request, sharefood_id):
    """User can delete share food event (only creating by their account)"""
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
             host_gender=request.user.info.get_gender(), host_number=request.user.info.get_number())   
            sp.save()
            return redirect('BetterTogetherApp:share_promotion_index1')

    context = {'form': form, 'date_time': DateForm}
    return render(request, 'BetterTogetherApp/share_promotion_create.html', context)

def delete_share_promotion(request, sharepromo_id):
    """User can delete share promotion event (only creating by their account)"""
    share = SharePromotion.objects.get(pk=sharepromo_id)
    share.delete()
    return redirect('BetterTogetherApp:share_promotion_index1')

@login_required
def create_share_ride(request):
    """User creates share ride event"""
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
             host_gender=request.user.info.get_gender(), host_number=request.user.info.get_number())   
            sr.save()
            return redirect('BetterTogetherApp:share_ride_index1')

    context = {'form': form, 'date_time': DateForm}
    return render(request, 'BetterTogetherApp/share_ride_create.html', context)

def delete_share_ride(request, shareride_id):
    """User can delete share ride event (only creating by their account)"""
    shareride1 = ShareRide.objects.get(pk=shareride_id)
    shareride1.delete()
    return redirect('BetterTogetherApp:share_ride_index1')

