from django import forms
from .models import Shifts, Availability

class WorkingHoursForm(forms.ModelForm):
	class Meta:
		model= Shifts
		fields= '__all__'
		labels = {
            "workhoursFrom": "From (HH/MM)",
            "workhoursTo": "To (HH/MM)",
        }

class AvailabilityForm(forms.ModelForm):
	class Meta:
		model=Availability
		fields={
			'availableDate'
		}
		widgets = {'availableDate': forms.DateInput()}
		labels={
			'availableDate': 'Change available date to: '
		}
