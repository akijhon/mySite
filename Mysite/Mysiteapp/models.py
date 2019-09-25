from django.db import models

# Create your models here.
class Images(models.Model):
    title = models.CharField(max_length=20)
    images = models.ImageField(upload_to='media/')

class Pimages(models.Model):
    title = models.CharField(max_length=20)
    images = models.ImageField(upload_to='media/')

class Pyobject(models.Model):
    title = models.CharField(max_length=20)
    url = models.URLField()
    image = models.ImageField(upload_to='language/')

class Jsobject(models.Model):
    title = models.CharField(max_length=20)
    url = models.URLField()
    image = models.ImageField(upload_to='language/')

class Phpobject(models.Model):
    title = models.CharField(max_length=20)
    url = models.URLField()
    image = models.ImageField(upload_to='language/')

class Rubyobject(models.Model):
    title = models.CharField(max_length=20)
    url = models.URLField()
    image = models.ImageField(upload_to='language/')
