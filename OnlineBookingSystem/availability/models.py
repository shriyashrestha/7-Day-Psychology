from django.db import models
from django.urls import reverse

from counsellor.models import Counsellor

import datetime
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

# Create your models here.

class Shifts(models.Model):
	workhoursFrom=models.TimeField(default=timezone.now)
	workhoursTo=models.TimeField(default=timezone.now)

	def get_absolute_url(self):
		return reverse("systemAdmin:list-workhours")

class Availability(models.Model):
	availableDate=models.DateField()
	counsellor= models.ForeignKey(Counsellor, on_delete=models.CASCADE, null='true')

	def get_absolute_url(self):
		return reverse("counsellor:my-availability")