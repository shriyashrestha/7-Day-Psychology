from django.db import models
from django import forms
from django.urls import reverse


# Create your models here.
class Client(models.Model):
    # max_length is a required field for char field
    # username of the client
    username = models.CharField(max_length=100)

    # login password of the user
    password = models.CharField(max_length=32, default="mydjango123")

    # username of the client
    name = models.CharField(max_length=100)

    # email address of the client
    email = models.EmailField(default='no_name@gmail.com')

    # phone number of the client
    phoneNumber = models.CharField(max_length=20)

    # description of the client
    description = models.TextField(blank='true', null='true')

    def get_absolute_url(self):
        return reverse("client:all-client-list")
