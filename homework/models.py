from django.db import models

# Create your models here.
class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class ToMeet(models.Model):
    persone = models.CharField(max_length=30)
    phone_number = models.IntegerField()  
    date_of_meeting = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    email = models.EmailField(max_length=20)
    company_name = models.CharField(max_length=30)