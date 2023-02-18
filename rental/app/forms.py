from django import forms
from .models import ProdBookingDetails

class XYZ_DateInput(forms.DateInput):
    input_type = "date"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        # kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)


class BookingForm(forms.ModelForm):
    class Meta:
        model=ProdBookingDetails
        fields = '__all__'
        widgets = {
            'bookdate': XYZ_DateInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],),
            'booking_end': XYZ_DateInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],),
        }   
        
