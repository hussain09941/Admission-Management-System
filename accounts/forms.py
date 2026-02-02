from django import forms
from django.contrib.auth.models import User

class StudentRegistratinForm(forms.ModelForm):
    password = forms.DecimalField(widget = forms.PasswordInput)
    confirm_password =forms.CharField(widget =forms.PasswordInput)

    class Meta:

        model= User
        fields = ['username','email','password']


    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') !=cleaned_data.get('confirm_password'):
            raise forms.ValidationError("Passworsd do not match")
        return cleaned_data