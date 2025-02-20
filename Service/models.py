from django.db import models

# Create your models here.

class service(models.Model):
    
    img1 = models.ImageField(upload_to='photos/', blank=True, null=True,max_length=200, )
 
    title= models.CharField(max_length=500, blank=True, null=True)
    paragraph= models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=1500, blank=True, null=True)
    img2 = models.ImageField(upload_to='photos/', blank=True, null=True,max_length=200, )