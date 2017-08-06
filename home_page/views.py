from django.shortcuts import *
from comment.forms import *
from django.http import *
from .models import *
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    a = request.user
    return render(request,"index.html",{'a':a})

def countries(request):
    return render(request,"Countries.html")

def month(request):
    month = Cities.objects.filter(Best_time_to_visit='january')
    if request.method == 'POST':
        mon = request.POST.get('select')
        month = Cities.objects.filter(Best_time_to_visit=mon)

        return render(request,'month.html',{'month':month})
    else:
        return render(request,"month.html",{'month':month})

def categories(request):
    Bdata = Cities.objects.filter(Type="Beaches")
    Adata = Cities.objects.filter(Type="Adventure")
    Mdata = Cities.objects.filter(Type="Mountains")
    Hdata = Cities.objects.filter(Type="Historical")
    return render(request,"categories.html",{'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata})

def aboutus(request):
    return render(request,"Aboutus.html")

def contactus(request):
    return render(request,"Contact.html")

def city(request,d,c):
    print d
    print c
    #post=comment.objects.order_by('-date_created')
    if request.method == 'POST':
        form = commentform(request.POST)

        if form.is_valid():
            a=form.save(commit=False)
            a.city=Cities.objects.get(Name=d)

            a.user=request.user

            a.save()
            c=c.lower()
            print c
            return redirect('home_page:'+c)


        else:
            return HttpResponse("Invalid comment")

    else:
        form=commentform()
    g=comment.objects.all()
    return render(request,'india.html',{'form':form, 'post':g})



def india(request):
    h=Countries.objects.get(Id='C1')
    Bdata = Cities.objects.filter(Id='C1',Type="Beaches")
    Adata = Cities.objects.filter(Id='C1',Type="Adventure")
    Mdata = Cities.objects.filter(Id='C1',Type="Mountains")
    Hdata = Cities.objects.filter(Id='C1',Type="Historical")
    form=commentform()
    return render(request,"india.html",{'form':form,'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata, 'data':h})


def china(request):
    h=Countries.objects.get(Id='C2')
    Bdata = Cities.objects.filter(Id='C2',Type="Beaches")
    Adata = Cities.objects.filter(Id='C2',Type="Adventure")
    Mdata = Cities.objects.filter(Id='C2',Type="Mountains")
    Hdata = Cities.objects.filter(Id='C2',Type="Historical")
    form=commentform()
    return render(request,"india.html",{'form':form,'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata, 'data':h})


def uae(request):
    h=Countries.objects.get(Id='C3')
    Bdata = Cities.objects.filter(Id='C3',Type="Beaches")
    Adata = Cities.objects.filter(Id='C3',Type="Adventure")
    Mdata = Cities.objects.filter(Id='C3',Type="Mountains")
    Hdata = Cities.objects.filter(Id='C3',Type="Historical")
    form=commentform()
    return render(request,"india.html",{'form':form,'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata, 'data':h})


def japan(request):
    h=Countries.objects.get(Id='C4')
    Bdata = Cities.objects.filter(Id='C4',Type="Beaches")
    Adata = Cities.objects.filter(Id='C4',Type="Adventure")
    Mdata = Cities.objects.filter(Id='C4',Type="Mountains")
    Hdata = Cities.objects.filter(Id='C4',Type="Historical")
    form=commentform()
    return render(request,"india.html",{'form':form,'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata, 'data':h})


def france(request):
    h=Countries.objects.get(Id='C5')
    Bdata = Cities.objects.filter(Id='C5',Type="Beaches")
    Adata = Cities.objects.filter(Id='C5',Type="Adventure")
    Mdata = Cities.objects.filter(Id='C5',Type="Mountains")
    Hdata = Cities.objects.filter(Id='C5',Type="Historical")
    form=commentform()
    return render(request,"india.html",{'form':form,'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata, 'data':h})


def greece(request):
    h=Countries.objects.get(Id='C6')
    Bdata = Cities.objects.filter(Id='C6',Type="Beaches")
    Adata = Cities.objects.filter(Id='C6',Type="Adventure")
    Mdata = Cities.objects.filter(Id='C6',Type="Mountains")
    Hdata = Cities.objects.filter(Id='C6',Type="Historical")
    form=commentform()
    return render(request,"india.html",{'form':form,'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata, 'data':h})


def sweden(request):
    h=Countries.objects.get(Id='C7')
    Bdata = Cities.objects.filter(Id='C7',Type="Beaches")
    Adata = Cities.objects.filter(Id='C7',Type="Adventure")
    Mdata = Cities.objects.filter(Id='C7',Type="Mountains")
    Hdata = Cities.objects.filter(Id='C7',Type="Historical")
    form=commentform()
    return render(request,"india.html",{'form':form,'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata, 'data':h})


def brazil(request):
    h=Countries.objects.get(Id='C8')
    Bdata = Cities.objects.filter(Id='C8',Type="Beaches")
    Adata = Cities.objects.filter(Id='C8',Type="Adventure")
    Mdata = Cities.objects.filter(Id='C8',Type="Mountains")
    Hdata = Cities.objects.filter(Id='C8',Type="Historical")
    form=commentform()
    return render(request,"india.html",{'form':form,'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata, 'data':h})


def argentina(request):
    h=Countries.objects.get(Id='C9')
    Bdata = Cities.objects.filter(Id='C9',Type="Beaches")
    Adata = Cities.objects.filter(Id='C9',Type="Adventure")
    Mdata = Cities.objects.filter(Id='C9',Type="Mountains")
    Hdata = Cities.objects.filter(Id='C9',Type="Historical")
    form=commentform()
    return render(request,"india.html",{'form':form,'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata, 'data':h})


def usa(request):
    h=Countries.objects.get(Id='C10')
    Bdata = Cities.objects.filter(Id='C10',Type="Beaches")
    Adata = Cities.objects.filter(Id='C10',Type="Adventure")
    Mdata = Cities.objects.filter(Id='C10',Type="Mountains")
    Hdata = Cities.objects.filter(Id='C10',Type="Historical")
    form=commentform()
    return render(request,"india.html",{'form':form,'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata, 'data':h})


def canada(request):
    h=Countries.objects.get(Id='C11')
    Bdata = Cities.objects.filter(Id='C11',Type="Beaches")
    Adata = Cities.objects.filter(Id='C11',Type="Adventure")
    Mdata = Cities.objects.filter(Id='C11',Type="Mountains")
    Hdata = Cities.objects.filter(Id='C11',Type="Historical")
    form=commentform()
    return render(request,"india.html",{'form':form,'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata, 'data':h})


def egypt(request):
    h=Countries.objects.get(Id='C12')
    Bdata = Cities.objects.filter(Id='C12',Type="Beaches")
    Adata = Cities.objects.filter(Id='C12',Type="Adventure")
    Mdata = Cities.objects.filter(Id='C12',Type="Mountains")
    Hdata = Cities.objects.filter(Id='C12',Type="Historical")
    form=commentform()
    return render(request,"india.html",{'form':form,'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata, 'data':h})


def madagascar(request):
    h=Countries.objects.get(Id='C13')
    Bdata = Cities.objects.filter(Id='C13',Type="Beaches")
    Adata = Cities.objects.filter(Id='C13',Type="Adventure")
    Mdata = Cities.objects.filter(Id='C13',Type="Mountains")
    Hdata = Cities.objects.filter(Id='C13',Type="Historical")
    form=commentform()
    return render(request,"india.html",{'form':form,'Bdata':Bdata,'Adata':Adata,'Mdata':Mdata,'Hdata':Hdata, 'data':h})
