
from django.shortcuts import render,redirect 
from .models import *

# Create your views here.

def index (request):
    return render(request,"index.html")
def reservation (request):
    return render(request, "reservation.html")

def InsertData(request):
    if request.method=="POST":
        fname=request.POST['Name']
        contact=request.POST['Phone']
        email=request.POST['Email']
        check_in=request.POST['Date_Check_In']
        check_out=request.POST['Date_Check_Out']
        adults=request.POST['Adulte']
        children=request.POST['Children']
        note=request.POST['Note']

        user=Reservation.objects.filter(Email=email)

        if user:
            message="User already Exist"
            return render(request,"index.html",{'msg':message})

    #creating object of model class
    #inserting data into table
        newuser=Reservation.objects.create(Name=fname,Phone=contact,Email=email,Date_Check_In=check_in,
                                        Date_Check_Out=check_out,Adulte=adults,Children=children,Note=note)
    #after insert render on showpage view
        newuser.save()
        return redirect('allRooms')


def contact(request):
    return  render (request, "contact.html")
def contactusData(request):
    if request.method=="POST":
        fname=request.POST['Name']
        contact=request.POST['Phone']
        email=request.POST['Email']
        note=request.POST['Note']

        newuser=ContactUs.objects.create(Name=fname,Phone=contact,Email=email,Note=note)

        newuser.save()
        return redirect('Thankyou')

def Thankyou(request):
    return  render (request, "Thankyou.html")

def blog (request):
    return render (request, "blog.html")
def about(request):
    return render (request, 'about.html')

def allRooms(request):
   return render(request, 'rooms.html')


def nagpurpage(request):
    return render (request, 'nagpur.html')

def delhipage(request):
    return render (request, 'delhi.html')

def mumbaipage(request):
    return render (request, 'mumbai.html')


