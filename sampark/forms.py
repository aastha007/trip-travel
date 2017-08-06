from django import forms
from django.contrib.auth.models import User
from .models import *

class contusform(forms.ModelForm):
    class Meta:
        model=contus
        fields='__all__'



class sugusform(forms.ModelForm):
    class Meta:
        model=sugus
        fields='__all__'
