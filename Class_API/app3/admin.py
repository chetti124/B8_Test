from django.contrib import admin

# Register your models here.

from .models import Student, Employee

admin.site.register([Student, Employee])
