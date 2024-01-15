from django.db import models

# Create your models here.

# Home page
class Slider(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='slider/')


class Info(models.Model):
    logo = models.ImageField(upload_to='logo/')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone_uz = models.CharField(max_length=255)
    phone_ru = models.CharField(max_length=255)
    phone_2 = models.CharField(max_length=255)
    email = models.EmailField()
    timetable = models.CharField(max_length=255)


class Product(models.Model):
    img = models.ImageField(upload_to='product/')
    name = models.CharField(max_length=255)
    description = models.TextField()



class Client(models.Model):
    name = models.CharField(max_length=255)
    idea = models.TextField()
    rate = models.IntegerField()


# About page

class About_model(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='about/')


class TeamMember(models.Model):
    img = models.ImageField(upload_to='team_members')
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)


# Services Page
    
class Statistics(models.Model):
    project_finished = models.IntegerField()
    client = models.IntegerField()
    hour_work = models.IntegerField()
    award_won = models.IntegerField()


class Background_Img(models.Model):
    img = models.ImageField(upload_to='bg/')
    img2 = models.ImageField(upload_to='bg/')


# Contact page
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()