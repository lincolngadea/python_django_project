from django import forms
from .models import User

# model Form

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome','telefone','email']


# form.Fom