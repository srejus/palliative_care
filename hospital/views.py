from django.shortcuts import render,redirect
from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from accounts.models import Account
from care_worker.models import CareWorker
from medical_worker.models import MedicalWorker
from .models import *

from palliative_care.utils import send_mail


# Create your views here.
@method_decorator(login_required, name='dispatch')
class EmergencyView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        Emergency.objects.create(user=acc)

        # send email noti

        subject = f"EMERGENCY REQUEST from {acc.full_name}!"
        content = f"New Emergency Request Created for {acc.full_name} from {acc.place} Phone: {acc.phone}\nPlease take necessary steps immediately\n\n\nThanks"

        medical_workers = MedicalWorker.objects.all()
        for medical_worker in medical_workers:
            try:
                send_mail(medical_worker.user.email,subject,content)
            except:
                pass

        msg = "Emergency Requested!"
        return redirect(f"/?msg={msg}")