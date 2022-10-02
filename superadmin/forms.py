from django import forms
from . models import Vehicle

class VehicleForm(forms.ModelForm):
    
    class Meta:
        model = Vehicle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
