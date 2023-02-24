from django.contrib import admin
from django.urls import path
from . import views

app_name='website'
urlpatterns = [
    path('' , views.homePage , name='home-page'),
    path('caravans/' , views.caravanList , name = 'all-caravans'),
    path('caravan/<caravan_id>' , views.show_details_of_caravans , name='caravan-detailes'),
    path('booking/<caravan_id>',views.bookCaravan ,name='booking'),
    path('showBook/', views.showUserbook , name='showBook'),
    path('addCaravan/' , views.addCaravan , name='addcaravan'),
    path('editcaravan/<caravan_id>',views.updateCaravan ,name='update'),
    path('delete/<caravan_id>',views.deleteCaravan, name='delete')

    
    
]
