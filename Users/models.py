from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    username=models.CharField(max_length=100)
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    email_address=models.CharField(max_length=100)
    type_of_service=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    Description=models.TextField()

    def submit(self):
        self.submit()
        self.save()

    def __str__(self):
        return self.name

class Vendors(models.Model):
    username=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    organization=models.CharField(max_length=100)
    organization_email=models.CharField(max_length=100)


    def submit(self):
        self.submit()
        self.save()


    def __str__(self):
        return self.name

