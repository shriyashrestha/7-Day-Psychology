from django.db import models
from django import forms
from django.urls import reverse
import datetime
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Counsellor(models.Model):
	# max_length is a required field for char field
	#name of ht counsellor
	name 		= models.CharField(max_length=100)

	#username of ht counsellor
	username 		= models.CharField(max_length=10)

	#login password of hte user
	password	= models.CharField(max_length=32,default="mydjango123")

	#address of the counsellor
	address		=models.CharField(max_length=200)

	# phone number of the counsellor
	phoneNumber =models.CharField(max_length=20)

	#email address of the counsellor
	email=models.EmailField(default='no_name@gmail.com')

	#education of the counsellor
	education	=models.TextField(blank='true', null='true')

	def get_absolute_url(self):
		return reverse('counsellor:all-counsellor-list')
