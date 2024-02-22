from django.db import models
from accounts.models import Account

# Create your models here.
class CareWorker(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='care_workers',null=True,blank=True)
    email = models.EmailField()
    description = models.TextField(null=True,blank=True)
    yrs_of_exp = models.IntegerField(default=0)
    place = models.CharField(max_length=100,null=True,blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

