from django.db import models

from counsellor.models import Counsellor

from client.models import Client

# Create your models here.
class Appointment(models.Model):
	appointmentDate=models.CharField(max_length=100)
	appointmentTime=models.CharField(max_length=100)
	counsellor= models.ForeignKey(Counsellor, on_delete=models.CASCADE, null='true')
	client= models.ForeignKey(Client, on_delete=models.CASCADE, null='true')