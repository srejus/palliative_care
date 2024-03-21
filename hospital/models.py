from django.db import models
from accounts.models import Account


# Create your models here.
class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField(null=True,blank=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    purpose = models.CharField(max_length=100,null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True,blank=True)


class Emergency(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='emergency_elder')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.full_name)+" > "+str(self.created_at)
