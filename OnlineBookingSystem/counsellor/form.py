from django import forms

from .models import Counsellor


class CounsellorForm(forms.ModelForm):
    class Meta:
        model = Counsellor
        fields = (
            'name',
            'username',
            'password',            
            'email',
            'phoneNumber',
            'address',
            'education'
        )
        widgets = {'password': forms.PasswordInput()}
        def clean(self):
            cleaned_data = super(CounsellorForm, self).clean()
            password = cleaned_data.get('password')
            if not password:
                raise forms.ValidationError('Need Password!')

