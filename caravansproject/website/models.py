from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Caravan (models.Model):
    name = models.CharField(max_length=512)
    feature_image=models.ImageField(upload_to="images/")
    description = models.TextField()
    price = models.IntegerField()
    capacity = models.IntegerField()
   



class Booking(models.Model):
    bookinUser = models.ForeignKey(User,on_delete=models.CASCADE)
    caravan = models.ForeignKey(Caravan, on_delete=models.CASCADE)
    Note=models.TextField()
    booking_date = models.DateTimeField()
    