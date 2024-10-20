from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model=Shop
        fields=['name','latitude','longitude']
    
    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude')
        if not(-90 <= latitude <=90):
            raise forms.ValidationError('Invalid latitude')
        return latitude
    
    def clean_longitude(self):
        longitude = self.cleaned_data.get('longitude')
        if not(-180 <= longitude <= 180):
            raise forms.ValidationError('Invalid longitude')
        return longitude