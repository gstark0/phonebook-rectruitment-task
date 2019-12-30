from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
 
class Phone(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.PROTECT)
    phone = models.CharField(max_length=50)
 
class Email(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.PROTECT)
    email = models.EmailField()