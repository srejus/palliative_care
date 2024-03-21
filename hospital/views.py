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
        care_worker_id = acc.care_worker_id
        medical_worker_id = acc.medical_worker_id

        subject = f"EMERGENCY REQUEST from {acc.full_name}!"
        content = f"New Emergency Request Created for {acc.full_name} from {acc.place} Phone: {acc.phone}\nPlease take necessary steps immediately\n\n\nThanks"

        if care_worker_id:
            try:
                care_worker = CareWorker.objects.get(id=care_worker_id)
                send_mail(care_worker.user.email,subject,content)
            except:
                pass

        if medical_worker_id:
            try:
                medical_worker = MedicalWorker.objects.get(id=medical_worker_id)
                send_mail(medical_worker.user.email,subject,content)
            except:
                pass

        msg = "Emergency Requested!"
        return redirect(f"/?msg={msg}")