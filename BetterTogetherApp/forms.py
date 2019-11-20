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
            'location_name': Textarea(attrs={'cols': 15, 'rows': 2}),
            'location': Textarea(attrs={'cols': 30, 'rows': 2}),
            'destination_name': Textarea(attrs={'cols': 30, 'rows': 2}),
            'destination': Textarea(attrs={'cols': 30, 'rows': 2}),
            'description': Textarea(attrs={'cols': 30, 'rows': 2}),
            'num_people': Textarea(attrs={'cols': 5, 'rows': 2}),
        }

class SharePromotionForm(forms.ModelForm):
    class Meta:
        model = SharePromotion
        fields = ['location_name', 'location', 'brand','description', 'num_people']
        widgets = {
            'location_name': Textarea(attrs={'cols': 15, 'rows': 2}),
            'location': Textarea(attrs={'cols': 30, 'rows': 2}),
            'brand': Textarea(attrs={'cols': 30, 'rows': 2}),
            'description': Textarea(attrs={'cols': 30, 'rows': 2}),
            'num_people': Textarea(attrs={'cols': 5, 'rows': 2}),
        }

class ShareFoodForm(forms.ModelForm):
    class Meta:
        model = ShareFood
        fields = ['location_name', 'location', 'description', 'num_people']
        widgets = {
            'location_name': Textarea(attrs={'cols': 15, 'rows': 2}),
            'location': Textarea(attrs={'cols': 30, 'rows': 2}),
            'description': Textarea(attrs={'cols': 30, 'rows': 2}),
            'num_people': Textarea(attrs={'cols': 5, 'rows': 2}),
        }
