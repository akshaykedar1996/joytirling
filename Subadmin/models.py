from django.db import models

# Create your models here.

import uuid
class Subadmin_user(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_email = models.EmailField(unique=True, blank=True, null=True)
    user_password = models.CharField(max_length=128, blank=True, null=True) 
    user_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
   
    

    
  
