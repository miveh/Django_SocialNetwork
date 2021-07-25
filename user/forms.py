from django.forms import ModelForm, forms
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' is email:
            raise forms.validationError('@ not in email!')
        return email
