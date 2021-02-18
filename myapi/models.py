from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Employee(models.Model):
	name = models.CharField(max_length=20)
	company= models.CharField(max_length=20)
	city = models.CharField(max_length=10)
	def __str__(self):
		return self.name;