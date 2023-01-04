from django.db import models


# Create your models here.
class Post(models.Model):
   Pinno =  models.CharField(max_length=12,blank=False,null=False)
   name = models.CharField(max_length=30,blank=False,null=False,default="my name")
   def __str__(self):
       return self.Pinno


   
