from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    DOB= models.DateField()
    male="m"
    female="f"
    NOTdefine="nf"
    gender=[(male,"male"),
            (female,"female"),   
            (NOTdefine,"notdefine")
    ]
    name =models.CharField(max_length=50)
    state =models.CharField(max_length=50,default="uttarperdesh")
    gender = models.CharField(max_length=2,choices=gender)
    phone= models.IntegerField()
    add=  models.CharField(max_length=500,default="user address" )
    city=models.CharField (max_length=40,default="enter your own city")

    def __str__(self):
            return '%s' % self.user.username 
    
   
