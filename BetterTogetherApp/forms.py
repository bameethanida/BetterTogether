from django import forms
from .models import ShareRide, SharePromotion
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

class SharePromotionForm(forms.ModelForm):
    class Meta:
        model = SharePromotion
        fields = ['location_name', 'location', 'brand','description', 'num_people']

