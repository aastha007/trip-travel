# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import *
from django.shortcuts import *
from django.views.generic import UpdateView,CreateView,DeleteView,DetailView,ListView
from django.core.urlresolvers import reverse,reverse_lazy
from home_page.models import *

# Create your views here.

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate (username=username, password=password)
        if user:
            login(request,user)
            return redirect('index')

        else:
            print("Someone Login and Failed!")
            print("Username:{} and Password:{}".format(username,password))
            return render(request,"login.html",{'invalid':True})

    else:
        return render(request,"login.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

class CountriesCreateView(CreateView):
    model= Countries
    fields='__all__'

class CountriesUpdateView(UpdateView):
    fields='__all__'
    model= Countries

class CountriesDeleteView(DeleteView):
    model = Countries
    success_url = reverse_lazy('index')
    context_object_name='country'


class CountriesDetailView(DetailView):
    model=Countries
    template_name='home_page/countries_details.html'
    context_object_name= 'country'


class CountriesListView(ListView):
    model=Countries
    context_object_name= 'countries_list'
