from django.db import models

# Create your models here.
class Reservation(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.IntegerField(default=0)
    Email = models.EmailField(max_length=40)
    Date_Check_In = models.DateField(null=True)
    Date_Check_Out  = models.DateField(null=True)
    Adulte = models.CharField (max_length=20)
    Children = models.CharField (max_length=20)
    Note = models.TextField()
    def __str__(self):
        return self.Name


class ContactUs(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.IntegerField(default=0)
    Email = models.EmailField(max_length=40)
    Note = models.TextField()
    def __str__(self):
        return self.Name
