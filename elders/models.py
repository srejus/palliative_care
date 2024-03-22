from django.db import models
from accounts.models import Account

# Create your models here.
class HealthRecord(models.Model):
    elder = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='elder_hr')
    created_by = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='created_by_hw')
    COL = "cholesterol"

    sugar = models.FloatField(null=True,blank=True)
    pressure = models.FloatField(null=True,blank=True)
    weight = models.FloatField(null=True,blank=True)
    cholesterol = models.FloatField(null=True,blank=True)
    notes = models.TextField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)