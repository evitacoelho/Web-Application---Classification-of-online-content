from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

User._meta.get_field('email')._unique = True

# Create your models here.


class Classifier(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, to_field = 'email')
    input = models.TextField()
    output = models.BooleanField()
    classificationCorrect = models.BooleanField(null=True)
    feedback = models.TextField(null=True)

class Locator(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, to_field = 'email')
    input = models.TextField()
    locOutput =  models.TextField()
    
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, to_field = 'email')
    input_image = models.TextField()
    output_image = models.BooleanField()
    classificationCorrect = models.BooleanField(null=True)
    feedback = models.TextField(null=True)