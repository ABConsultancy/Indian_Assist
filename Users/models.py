from django.db import models
from django_countries.fields import CountryField

class NRI(models.Model):
    username=models.CharField(max_length=100)
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    email_address=models.EmailField(max_length=100)
    type_of_service=models.CharField(max_length=100)
    country=CountryField()
    budget=models.IntegerField(null=True)
    Description=models.TextField()

    def submit(self):
        self.submit()
        self.save()

    def __str__(self):
        return self.name

class Vendor(models.Model):
    username=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    organization=models.CharField(max_length=100)
    organization_email=models.CharField(max_length=100)


    def submit(self):
        self.submit()
        self.save()


    def __str__(self):
        return self.name
