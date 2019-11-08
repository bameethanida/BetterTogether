from django import forms
from .models import ShareRide

class ShareRideForm(forms.ModelForm):
    class Meta:
        model = ShareRide
        fields = ['location','destination','description','date_time', 'num_people']
