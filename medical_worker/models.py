from django.db import models
from accounts.models import Account

# Create your models here.
class MedicalWorker(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='medical_worker',null=True,blank=True)
    email = models.EmailField()
    description = models.TextField(null=True,blank=True)
    yrs_of_exp = models.IntegerField(default=0)
    place = models.CharField(max_length=100,null=True,blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class RequestHwHiring(models.Model):
    REQ_STATUS = (
        ('SENT','SENT'),
        ('ACCEPTED','ACCEPTED'),
        ('REJECTED','REJECTED'),
    )
    user = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='hw_requested_user')
    hw = models.ForeignKey(MedicalWorker,on_delete=models.CASCADE,related_name='requested_hw')
    status = models.CharField(max_length=25,default='SENT',choices=REQ_STATUS)
    needs = models.TextField(null=True,blank=True)
    medical_req = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.full_name)