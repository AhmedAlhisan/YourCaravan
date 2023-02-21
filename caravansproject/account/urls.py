from django.urls import path
from . import views
app_name='account'
urlpatterns = [
    path('ac', views.signup, name='register'),
        path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        views.activate, name='activate'),
]