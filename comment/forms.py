from django import forms
from .models import *
from django.contrib.auth.models import User


class commentform(forms.ModelForm):
    title=forms.CharField(required=True)
    class Meta():
        model=comment
        fields=('title','comment_box')
