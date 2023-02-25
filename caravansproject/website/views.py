from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from . models import Caravan , Booking , ContactUs
from django.contrib import messages
from django.contrib.auth.models import Group , User 
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

def addCaravanAdmin(request :HttpRequest):
    '''this function will allow admin to add th caravan directly without confirmation'''
    '''add new caravan by admin '''
    if request.user.is_staff:
        if request.method == 'POST':
            new_caravan=Caravan(name=request.POST['name'],feature_image=request.FILES['feature_image'],description=request.POST['description'],price=request.POST['price'],capacity=request.POST['capacity'],owner=request.user, carvan_status=True)
            new_caravan.save()
        return render(request , 'website/adminAddCaravan.html') 
    return redirect('account:login')

def addCaravanuser(request :HttpRequest):
    '''this function will allow users to add the caravan but still need  confirmation from admin'''
    '''add new caravan by user '''
    if request.user.is_authenticated:
        if request.method == 'POST':
            new_caravan=Caravan(name=request.POST['name'],feature_image=request.FILES['feature_image'],description=request.POST['description'],price=request.POST['price'],capacity=request.POST['capacity'],owner=request.user, carvan_status=False)
            new_caravan.save()
            investor_group = Group.objects.get(name='user-Investor')
            request.user.groups.add(investor_group)
        return render(request , 'website/adminAddCaravan.html')
    return redirect('account:login')        

def show_details_of_caravans(request :HttpRequest , caravan_id):
    if request.user.is_authenticated:
        assigend_caravan = Caravan.objects.get(id = caravan_id)
        return render(request , 'website/caravan-single.html' , {'assigend_caravan':assigend_caravan})
    return redirect('account:login')

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

def showNeedConfirmationCaravans(request : HttpRequest):
    '''this function will show all caravans poted by users , and admin need to confirm this caravans to show four public'''
    if request.user.is_staff:
        pending_caravan=Caravan.objects.filter(carvan_status = False)
        return render(request , 'website/AdminShowAllpending.html' , {'pending_caravan':pending_caravan})
    return redirect('account:login')

def showSelctedCarvanDetailsByAdminToConfirm(request : HttpRequest , caravan_id):
    '''show detailes of one pending caravan'''
    if request.user.is_staff:
        assigend_caravan = Caravan.objects.get(id = caravan_id)
        return render(request , 'website/showSelctedCarvanDetailsByAdminToConfirm.html' , {'assigend_caravan':assigend_caravan} )


def confirmCaravan(request : HttpRequest , caravan_id):
    '''confirmation the caravan'''
    if request.user.is_staff:        
        assigend_caravan = Caravan.objects.get(id=caravan_id)
        assigend_caravan.carvan_status=True
        assigend_caravan.save()
        messages.success(request , 'caravan Status is now Active and accepted')
        return redirect('website:home-page')
def rejectCaravan(request : HttpRequest , caravan_id):
    '''reject Caravan and delete it'''
    if request.user.is_staff:
        assigend_caravan  =Caravan.objects.get(id=caravan_id)
        assigend_caravan.delete()
        messages.success(request , 'caravan status is Un-Active and rejected' )
        return redirect('website:home-page')


def showCaravanStatusUser(request : HttpRequest):
    inestor_user_caravan = Caravan.objects.filter(  owner = request.user.id)
    return render(request , 'website/userAddCaravanStatus.html' , {'inestor_user_caravan':inestor_user_caravan})

def adminManagAllCravanBook(request : HttpRequest , caravan_id):
    if request.user.is_staff:
        assigend_caravan = Caravan.objects.get(id = caravan_id)
        all_users_booking = Booking.objects.filter(caravan = assigend_caravan)
        return render(request , 'website/showAllUsersBookInEachCaravan.html' , {'all_users_booking':all_users_booking ,'assigend_caravan':assigend_caravan })
    return redirect('website:home')


            
    
   
        











    
