from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from . models import Caravan , Booking
from django.contrib import messages

# Create your views here.

def homePage(request :HttpRequest):
    return render(request , 'website/home.html')

def caravanList(request :HttpRequest):
    if 'search' in request.GET:
        all_carvans = Caravan.objects.filter(name__contains=request.GET["search"])
    else:
        all_carvans = Caravan.objects.all()
        
    return render(request , 'website/caravan-grid.html' , {'all_carvans':all_carvans})


def show_details_of_caravans(request :HttpRequest , caravan_id):
    assigend_caravan = Caravan.objects.get(id = caravan_id)
    return render(request , 'website/caravan-single.html' , {'assigend_caravan':assigend_caravan})

def bookCaravan(request :HttpRequest , caravan_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
             
            assigend_caravan = Caravan.objects.get(id=caravan_id)
            new_book = Booking(bookinUser = request.user , caravan = assigend_caravan ,Note=request.POST['Note'],booking_date = request.POST['booking_date'] )
            check_dateTime = Booking.objects.filter(booking_date = request.POST['booking_date'])
            
            if check_dateTime :
                messages.success(request , 'soory chose another date and time')

            else:      
                new_book.save()
                messages.success(request, 'Your booking is succesfuly Done , Thank you')
                return redirect('website:home-page')
            
            
    return render(request,'website/book-caravan.html')



    
