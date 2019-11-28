from django import forms
from django.forms import Textarea
from .models import ShareRide, SharePromotion, ShareFood
from datetime import datetime

myDate = datetime.now()
time = myDate.strftime("%H:%M:%S")
date = myDate.strftime("%Y-%m-%d")

class DateForm(forms.Form):
    day = forms.DateField(initial=date)
    time = forms.TimeField(initial=time)
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
