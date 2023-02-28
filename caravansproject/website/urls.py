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
    path('addCaravanAdmin/' , views.addCaravanAdmin , name='addcaravanadmin'),
    path('addCaravanUser/' , views.addCaravanuser , name='addcaravanuser'),
    path('editcaravan/<caravan_id>',views.updateCaravan ,name='update'),
    path('delete/<caravan_id>',views.deleteCaravan, name='delete'),
    path('showAllPending/' , views.showNeedConfirmationCaravans,name='PendingCaravans'),
    path('showOnePending/<caravan_id>', views.showSelctedCarvanDetailsByAdminToConfirm , name='pendingCaravan'),
    path("confirmCaravan/<caravan_id>" , views.confirmCaravan , name='confirmation'),
    path("rejectCaravan/<caravan_id>" , views.rejectCaravan , name='reject'),
    path('showCaravanStatusUser' , views.showCaravanStatusUser , name='showCaravanStatusUser'),
    path('adminManagAllCravanBook/<caravan_id>',views.adminManagAllCravanBook , name='adminManageBook'),
    path('deleteBookingByAdmin/<book_id>',views.adminDeleteBooking , name='deleteBookingAdmin'),
    path('updateBookingByAdmin/<book_id>',views.adminUpdateingBook , name='updatingBooking'),
    path('showUserCaravanStatusBooking/<carvan_id>' , views.showUserCaravanIsBookStatus , name='showUserCaravanIsBookStatus'),
    

     
    

    
    
]
