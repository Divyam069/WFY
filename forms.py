from django import forms
from Div.models import Register

class UserRegisterForm(forms.Modelform):
    class Meta:
        model=Register
        fields='__all__'