# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from .forms import *
from django.shortcuts import render

# Create your views here.

def register(request):
    registered = False
    if request.method == 'POST':
        user_form= NewUserForm(request.POST)
        profile_form= ProfileInfo(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True

        else:
            print (user_form.errors,profile_form.errors)

    else:
        user_form = NewUserForm()
        profile_form = ProfileInfo()

    return render(request,'register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
