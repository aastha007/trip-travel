# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import *
from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
'''
def com(request):
    print "hello"
    post=comment.objects.order_by('-date_created')
    if request.method== 'POST':
        form = commentform(request.POST)

        if form.is_valid():
            a=form.save(commit=False)
            a.user=request.user
            a.save()
            #return HttpResponseRedirect('/comment/')

        else:
            return HttpResponse("Invalid comment")

    else:
        form=commentform()
        print form
    return render(request,'india.html',{'form':form,'post':post})
'''
