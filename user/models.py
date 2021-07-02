from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    DOB= models.DateField()
    
    name =models.CharField(max_length=50)
    img=models.ImageField(upload_to='media/img', default='no img')
    gender = models.CharField(max_length=6)
    phone= models.IntegerField()
   
    def __str__(self):
            return '%s' % self.user.username 
    
    
    
    
class Adderss(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        add=  models.CharField(max_length=500,default="user address" )
        city=models.CharField (max_length=40,default="enter your own city")
        zipcode=models.IntegerField()
        state =models.CharField(max_length=50,default="uttarperdesh")
