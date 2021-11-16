from django.db import models

# Create your models here.
class Admin(models.Model):
    username=models.CharField(max_length=100, default="admin")
    password=models.CharField(max_length=100, default="admin")
