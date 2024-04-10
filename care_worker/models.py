from django.db import models
from accounts.models import Account

# Create your models here.
class CareWorker(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='care_workers',null=True,blank=True)
    email = models.EmailField()
    age = models.IntegerField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    yrs_of_exp = models.IntegerField(default=0)
    place = models.CharField(max_length=100,null=True,blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



class RequestCwHiring(models.Model):
    REQ_STATUS = (
        ('SENT','SENT'),
        ('ACCEPTED','ACCEPTED'),
        ('REJECTED','REJECTED'),
    )
    user = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='cw_requested_user')
    cw = models.ForeignKey(CareWorker,on_delete=models.CASCADE,related_name='requested_cw')
    status = models.CharField(max_length=25,default='SENT',choices=REQ_STATUS)
    needs = models.TextField(null=True,blank=True)
    medical_req = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.full_name)