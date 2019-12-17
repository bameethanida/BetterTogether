from django import forms
from django.forms import Textarea, DateInput
from .models import ShareRide, SharePromotion, ShareFood, Info
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm

myDate = datetime.now()
time = myDate.strftime("%H:%M:%S")
date = myDate.strftime("%Y-%m-%d")

class DateForm(forms.Form):
    day = forms.CharField(initial=date)
    time = forms.CharField(initial=time)
    fields = ['day','time']

class ShareRideForm(forms.ModelForm):
    class Meta:
        model = ShareRide
        fields = ['location_name','location','destination_name','destination','description', 'num_people']
        widgets = {
            'location_name': Textarea(attrs={'cols': 15, 'rows': 2, 'placeholder': 'Paragon'}),
            'location': Textarea(attrs={'cols': 30, 'rows': 2, 'placeholder': '991 Rama 1 Road, Pathumwan Subdistrict, Pathumwan District, Bangkok 10330'}),
            'destination_name': Textarea(attrs={'cols': 30, 'rows': 2,'placeholder': 'Central World' }),
            'destination': Textarea(attrs={'cols': 30, 'rows': 2,'placeholder': '999/9 Rama I Rd, Pathum Wan, Pathum Wan District, Bangkok 10330'}),
            'description': Textarea(attrs={'cols': 30, 'rows': 2, 'placeholder': 'Description'}),
            'num_people': Textarea(attrs={'cols': 5, 'rows': 2}),
        }

class SharePromotionForm(forms.ModelForm):
    class Meta:
        model = SharePromotion
        fields = ['location_name', 'location', 'brand','description', 'num_people']
        widgets = {
            'location_name': Textarea(attrs={'cols': 15, 'rows': 2,'placeholder':'Central Ladprao'}),
            'location': Textarea(attrs={'cols': 30, 'rows': 2,'placeholder':'1693 Phahonyothin Rd, Chatuchak, Bangkok 10900'}),
            'brand': Textarea(attrs={'cols': 30, 'rows': 2,'placeholder':'Zara'}),
            'description': Textarea(attrs={'cols': 30, 'rows': 2,'placeholder':'Description'}),
            'num_people': Textarea(attrs={'cols': 5, 'rows': 2}),

        }

class ShareFoodForm(forms.ModelForm):
    class Meta:
        model = ShareFood
        fields = ['location_name', 'location', 'description', 'num_people']
        widgets = {
            'location_name': Textarea(attrs={'cols': 15, 'rows': 2,'placeholder': 'Kuma Shabu'}),
            'location': Textarea(attrs={'cols': 30, 'rows': 2,'placeholder': '21 30 Thanon Ngamwongwan, Lat Yao, Chatuchak, Bangkok 10900'}),
            'description': Textarea(attrs={'cols': 30, 'rows': 2,'placeholder': 'Description'}),
            'num_people': Textarea(attrs={'cols': 5, 'rows': 2}),
        }

class EditInfo(forms.ModelForm):
    birthday = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1940, 2020)))
    class Meta:
        model = Info
        fields = ['gender', 'birthday', 'brief_info', 'phone_num', 'twitter']
        widgets = {
            'gender': Textarea(attrs={'cols': 15, 'rows': 2}),
            'brief_info': Textarea(attrs={'cols': 30, 'rows': 2}),
            'phone_num': Textarea(attrs={'cols': 15, 'rows': 2}),
            'twitter': Textarea(attrs={'cols': 25, 'rows': 2})
        }

class SignIn(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        

class SignUp(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'password1': Textarea(attrs={'cols': 15, 'rows': 2}),
            'password2': Textarea(attrs={'cols': 15, 'rows': 2}),
            'first_name': Textarea(attrs={'cols': 15, 'rows': 2}),
            'last_name': Textarea(attrs={'cols': 15, 'rows': 2})
        }