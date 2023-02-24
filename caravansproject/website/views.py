from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from . models import Caravan , Booking , ContactUs
from django.contrib import messages

from django.conf import settings



# Create your views here.

def homePage(request :HttpRequest):
    return render(request , 'website/home.html')

def caravanList(request :HttpRequest):
    
    if 'search' in request.GET:
        all_carvans = Caravan.objects.filter(name__contains=request.GET["search"]).filter(carvan_status = True)
    else:
        all_carvans = Caravan.objects.filter(carvan_status = True)
        
    return render(request , 'website/caravan-grid.html' , {'all_carvans':all_carvans})

def addCaravan(request :HttpRequest):
    '''add new caravan by admin '''
    if request.user.is_staff:
        if request.method == 'POST':
            new_caravan=Caravan(name=request.POST['name'],feature_image=request.FILES['feature_image'],description=request.POST['description'],price=request.POST['price'],capacity=request.POST['capacity'],owner=request.user, carvan_status=True)
            new_caravan.save()
        return render(request , 'website/adminAddCaravan.html')    

def show_details_of_caravans(request :HttpRequest , caravan_id):
    assigend_caravan = Caravan.objects.get(id = caravan_id)
    return render(request , 'website/caravan-single.html' , {'assigend_caravan':assigend_caravan})

def bookCaravan(request :HttpRequest , caravan_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
             
            assigend_caravan = Caravan.objects.get(id=caravan_id)
            new_book = Booking(bookinUser = request.user , caravan = assigend_caravan ,note=request.POST['Note'],booking_date = request.POST['booking_date'] )
            check_dateTime = Booking.objects.filter(booking_date = request.POST['booking_date'])
            
            if check_dateTime :
                messages.success(request , 'soory chose another date and time')

            else:      
                new_book.save()
                messages.success(request, 'Your booking is succesfuly Done , Thank you ')
                return redirect('website:home-page')
            
            
    return render(request,'website/book-caravan.html')


def showUserbook(request : HttpRequest ):
    if request.user.is_authenticated:
        bookinUser = request.user.get_username    
        show_booked = Booking.objects.filter(bookinUser = request.user.id)
        return render(request , 'website/show-user-book.html', {'show_booked':show_booked , 'bookinUser':bookinUser})
    return redirect('account:login')


def updateCaravan(request : HttpRequest , caravan_id):
    if request.user.is_staff:
        selected_caravan = Caravan.objects.get(id=caravan_id)
        if request.method == 'POST':
            if 'name' in request.POST:
                selected_caravan.name = request.POST['name']
            if 'description' in request.POST:
                selected_caravan.description=request.POST['description']
            if 'price' in request.POST:
                selected_caravan.price = request.POST['price']
            if 'capacity' in request.POST:
                selected_caravan.capacity=request.POST['capacity']
            if 'carvan_status' in request.POST:
                selected_caravan.carvan_status=request.POST['carvan_status']
            if "feature_image" in request.FILES:
                selected_caravan.feature_image=request.POST['feature_image']
            selected_caravan.save()
            messages.success(request , 'selected Caravan updated succesfuly')
        return render(request , 'website/adminEditCaravan.html' , {'selected_caravan':selected_caravan}) 
    return redirect('website:home-page')

def deleteCaravan(request: HttpRequest , caravan_id):
    if request.user.is_staff:
        selected_caraven = Caravan.objects.get(id=caravan_id)
        selected_caraven.delete()   
        messages.success(request , 'selected Caravan , deleted succesfuly')
        return redirect('website:home-page')        






    
