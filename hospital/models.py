from django.db import models
from accounts.models import Account

from medical_worker.models import MedicalWorker


# Create your models here.
class Appointment(models.Model):
    RECEIVED = 'RECEIVED'
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'

    STATUS_CHOCIES = (
        (RECEIVED,RECEIVED),
        (ACCEPTED,ACCEPTED),
        (REJECTED,REJECTED)
    )
    hw = models.ForeignKey(MedicalWorker,on_delete=models.CASCADE,related_name='health_worker')
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField(null=True,blank=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    purpose = models.CharField(max_length=100,null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=15,default=RECEIVED,choices=STATUS_CHOCIES)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True,blank=True)


class Emergency(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='emergency_elder')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.full_name)+" > "+str(self.created_at)
