from django.db import models

# Create your models here.


class Employee(models.Model):
    pass

class Student(models.Model):
    name =models.CharField(max_length=200)
    age = models.IntegerField()
    marks = models.IntegerField()
    address = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "student"



class Employee(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    salary = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "employee"


# to creaate token automatically from admin page when we create new user using signals.

from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


# This code is triggered whenever a new student has been created and saved to the database
@receiver(post_save, sender=Student)
def welcome(sender, instance=None, created=False, **kwargs): # True
    print(created)
    if created:
        print(f"Welcome {instance.name}")
        

# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        print("Token")  # implememt email and send token on mail to user
        Token.objects.create(user=instance)

