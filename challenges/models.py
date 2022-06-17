from django.db import models

class blazers(models.Model):
    link= models.URLField(max_length = 500)
    seller = models.CharField(max_length = 200)
    price = models.IntegerField(null=True)
    name = models.CharField(null=True, max_length=200)
class shirts(models.Model):
    link= models.URLField(max_length = 500)
    seller = models.CharField(max_length = 200)
    price = models.IntegerField(null=True)
    name = models.CharField(null=True, max_length=200)
class sweaters(models.Model):
    link= models.URLField(max_length = 500)
    seller = models.CharField(max_length = 200)
    price = models.IntegerField(null=True)
    name = models.CharField(null=True, max_length=200)
class t_shirts(models.Model):
    link= models.URLField(max_length = 500)
    seller = models.CharField(max_length = 200)
    price = models.IntegerField(null=True)
    name = models.CharField(null=True, max_length=200)