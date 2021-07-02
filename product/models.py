from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields.related import ForeignKey


# Create your models here.


class Products(models.Model):
    product_category = (
        ('wedding', 'wedding'),
        ('brithday', 'brithday'),
        ('photoshot', 'photoshot'),
        ('themes','themes')
    )
    name = models.CharField(max_length=50, default="user name")
    image = models.ImageField(upload_to='products', default='there is no image')
    detail = models.TextField(max_length=1000)
    price = models.IntegerField(default=0)
    cat = models.CharField(max_length=10, choices=product_category, default=product_category[0][1])
    quantity = models.IntegerField(default=100)
    discount=models.FloatField(default=.05)
    add_no = models.DateField(auto_now=True)
    total=models.IntegerField(default=0)    
   
    def __str__(self):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=500)
    img=models.ImageField(upload_to='img', default='no img')


'''
class Purchase(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    products=models.ForeignKey(Products,on_delete=CASCADE)
    price= models.IntegerField()
    quantity=models.IntegerField()
    
    

'''


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
