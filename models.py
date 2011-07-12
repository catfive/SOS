from django.db import models
from django.contrib.auth.models import User

# Create your models here.
	
class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=255)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	manufacturer = models.CharField(max_length=100, blank=True)
	
	def __unicode__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.name
			
class Location(models.Model):
	name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name

class SOSuser(User):
	department = models.ManyToManyField(Department)
	location = models.ManyToManyField(Location)