from django.contrib import admin
from django.urls import path
from . import views
app_name='website'
urlpatterns = [
    path('' , views.homePage , name='home-page'),
    path('caravans/' , views.caravanList , name = 'all-caravans'),
    path('caravan/<caravan_id>' , views.show_details_of_caravans , name='caravan-detailes')
    
]
