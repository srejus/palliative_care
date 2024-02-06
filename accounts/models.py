from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    USER_TYPE_CHOICES = (
        ('ELDER','ELDER'),
        ('CARE_WORKER','CARE_WORKER'),
        ('HEALTH_WORKER','HEALTH_WORKER'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15,null=True,blank=True)
    user_type = models.CharField(max_length=20,default='ELDER')
    address = models.CharField(max_length=250,null=True,blank=True)
    place = models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return str(self.full_name)