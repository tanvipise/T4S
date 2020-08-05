from django.db import models

# Create your models here.


class Client(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    about = models.TextField()
    experience = models.BigIntegerField()
    skills = models.TextField()
    location = models.TextField()


class Coach_sessions(models.Model):
    session_details = models. TextField()

    no_of_quiz = models.BigIntegerField()
    hrs_of_quiz = models.BigIntegerField()

    no_of_video = models.BigIntegerField()
    hrs_of_video = models.BigIntegerField()

    no_of_music = models.BigIntegerField()
    hrs_of_music = models.BigIntegerField()

    no_of_images = models.BigIntegerField()
    hrs_of_images = models.BigIntegerField()
