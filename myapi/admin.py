from django.contrib import admin

# Register your models here.
from .models import Hero, Employee

admin.site.register(Employee)
admin.site.register(Hero)

