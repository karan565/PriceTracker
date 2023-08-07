from django.shortcuts import render, HttpResponse
import datetime
import urllib.request as urllib2
from bs4 import BeautifulSoup
from django.contrib import messages
from .models import *
import time
from .tasks import send_email_task
from django.http import JsonResponse

# Create your views here.


def pricetracker(request):
    send_email_task()
    return JsonResponse({'message': 'Function called'})


def index(request):
    # return HttpResponse(datetime.datetime.now())
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')


def amazon(request):
    return render(request, 'amazon.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def flipkart(request):
    return render(request, 'flipkart.html')


def registers(request):
    if request.method == "POST":
        pname = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        targetprice = request.POST.get('targetprice')
        link = request.POST.get('link')
        Register = register(name=pname, email=email,
                            phone=phone, targetprice=targetprice, link=link)
        Register.save()
        messages.success(
            request, 'Your data has been saved and will notify you once you targetted price is achieved !')
    return render(request, 'home.html')
