from django.db import models

# Create your models here.


class Formalshirts(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=1000)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    avalable=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class CasualShirt(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    avalable=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Pants(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    avalable=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
    
