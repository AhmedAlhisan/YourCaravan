from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . models import Caravan , Booking

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


    
