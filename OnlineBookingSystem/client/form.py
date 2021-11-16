from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'name',
            'username',
            'password',
            'email',
            'phoneNumber',
            'description',
        )
        widgets = {'password': forms.PasswordInput()}
        def clean(self):
            cleaned_data = super(ClientForm, self).clean()
            password = cleaned_data.get('password')
            if not password:
                raise forms.ValidationError('Need Password!')

