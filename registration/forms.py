from django import forms
from django.contrib.auth.models import User
from .models import *
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class NewUserForm(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput
                (attrs={'class':'reg-form'}),max_length=30,required=True)

    last_name=forms.CharField(widget=forms.TextInput
                (attrs={'class':'reg-form'}),max_length=30,required=True)

    username=forms.CharField(widget=forms.TextInput
                (attrs={'class':'reg-form'}),max_length=30,required=True,validators=[alphanumeric])

    email=forms.CharField(widget=forms.EmailInput
                (attrs={'class':'reg-form'}),max_length=30,required=True)

    password = forms.CharField(widget=forms.PasswordInput
                (attrs={'class':'reg-form'}),max_length=30,required=True)

    confirm_password = forms.CharField(widget = forms.PasswordInput(),required=True)

    botcatcher = forms.CharField(required=False,widget = forms.HiddenInput)

    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password','confirm_password')

    def clean_username(self):
        uname=self.cleaned_data['username']
        try:
            match = User.objects.get(username=uname)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError('Username already exist')

    def clean_email(self):
        mail= self.cleaned_data['email']
        print mail
        try:
            match = User.objects.get(email=mail)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError('Email already exist')

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError("Your passwords did not match!")


    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("Sorry no Bots allowed!")




class ProfileInfo(forms.ModelForm):
    class Meta():
        model=NewUser
        fields=('profile_pic',)
