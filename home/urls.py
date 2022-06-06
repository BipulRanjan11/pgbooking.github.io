from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',index, name= 'index'),
    path ("Reservation",reservation,name= 'reservation'),
    path("insert/",InsertData,name="insert"),
    path ("Contact",contact,name= 'contact'),
    path ("contact",contactusData,name= 'contactus'),
    path ("thanks",Thankyou,name= 'Thankyou'),
    path ("Blog",blog,name= 'blog'),
    path ("About",about,name= 'about'),
    path("allRooms",allRooms, name= 'allRooms'),
    path ("Nagpur",nagpurpage,name= 'nagpur'),
    path ("Delhi",delhipage,name= 'delhi'),
    path ("Mumbai",mumbaipage,name= 'mumbai'),
]
urlpatterns += staticfiles_urlpatterns()
