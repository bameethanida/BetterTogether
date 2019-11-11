from django import forms
from .models import ShareRide

class ShareRideForm(forms.ModelForm):
    class Meta:
        model = ShareRide
        fields = ['location_name','location','destination_name','destination','description','date_time', 'num_people']
