from django.shortcuts import render,redirect
from sampark.forms import *
from django.http import *
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method=='POST':
        contact_us=contusform(request.POST)

        if contact_us.is_valid():
            cont=contact_us.save()
            return redirect('contact')
        else:
            print(contact_us.errors)
    else:
        contact_us=contusform()
    return render(request,'contact.html',{'contactus':contact_us})


def suggest(request):
    if request.method=='POST':
        suggest_us=sugusform(request.POST)
        print 'hello'
        if suggest_us.is_valid():
            sug=suggest_us.save()
            send_mail(
                'New Suggestion',
                'You have got new suggestion!!!',
                'triptravel321@gmail.com',
                ['arpitg276@gmail.com','aastha7195@gmail.com','gaganjuneja2010@gmail.com'],
                fail_silently=False,)
            return redirect('suggest')

        else:
            print(suggest_us.errors)
    else:
        suggest_us=sugusform()
    return render(request, 'suggest.html',{'suggest_us':suggest_us})
