from django.db import models

# Create your models here.


class Client(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    about = models.TextField()
    experience = models.BigIntegerField()
    skills = models.TextField()
    location = models.TextField()
