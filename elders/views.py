from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse

from care_worker.models import CareWorker,RequestCwHiring
from hospital.models import Appointment
from medical_worker.models import MedicalWorker,RequestHwHiring
from accounts.models import Account


# Create your views here.
@method_decorator(login_required, name='dispatch')
class ElderHomeView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        if acc.user_type != 'ELDER':
            msg = "Only Elder user can access this page!"
            return redirect(f"/?msg={msg}")
        
        msg = request.GET.get("msg")
        return render(request,'elders/elder_home.html',{'msg':msg})
    

@method_decorator(login_required, name='dispatch')
class FindCareWorkerView(View):
    def get(self,request,id=None):
        care_workers = CareWorker.objects.filter(is_approved=True)
        if id:
            worker = care_workers.get(id=id)
            return render(request,'elders/care_worker_details.html',{'worker':worker})
        return render(request,'elders/find_care_worker.html',{'care_workers':care_workers})
    

@method_decorator(login_required,name='dispatch')
class SendCareWorkerReqView(View):
    def get(self,request,id):
        return render(request,'elders/elder_req.html')

    def post(self,request,id):
        cw = CareWorker.objects.get(id=id)
        acc = Account.objects.get(user=request.user)

        needs = request.POST.get("needs")
        medical_needs = request.POST.get("medical_requirements")

        RequestCwHiring.objects.create(user=acc,cw=cw,needs=needs,medical_req=medical_needs)

        msg = 'Hire request sent successfully!'
        return redirect(f"/elders/?msg={msg}")
    

@method_decorator(login_required,name='dispatch')
class SendHealthWorkerReqView(View):
    def get(self,request,id):
        return render(request,'elders/elder_req.html')

    def post(self,request,id):
        hw = MedicalWorker.objects.get(id=id)
        acc = Account.objects.get(user=request.user)

        needs = request.POST.get("needs")
        medical_needs = request.POST.get("medical_requirements")

        RequestHwHiring.objects.create(user=acc,hw=hw,needs=needs,medical_req=medical_needs)

        msg = 'Hire request sent successfully!'
        return redirect(f"/elders/?msg={msg}")
    

@method_decorator(login_required, name='dispatch')
class FindMedicalWorkerView(View):
    def get(self,request,id=None):
        medical_workers = MedicalWorker.objects.filter(is_approved=True)
        if id:
            worker = medical_workers.get(id=id)
            return render(request,'medical_worker_details.html',{'worker':worker})
        return render(request,'find_health_worker.html',{'care_workers':medical_workers})

    

@method_decorator(login_required, name='dispatch')
class SendHiringRequestToCareWorkerView(View):
    def get(self,request,id):
        cw = CareWorker.objects.get(id=id)
        acc = Account.objects.get(user=request.user)
        RequestCwHiring.objects.create(user=acc,cw=cw)
        return HttpResponse("Request sent successfully!")
    

@method_decorator(login_required, name='dispatch')
class SendHiringRequestToMedcialWorkerView(View):
    def get(self,request,id):
        print("----Sending Request to Hiring Medical Worker-------")
        return HttpResponse("Request sent successfully!")
    

@method_decorator(login_required, name='dispatch')
class BookAppointmentView(View):
    def get(self,request):
        return render(request,'elders/book_appointment.html')

    def post(self,request):
        patient_name = request.POST.get("name")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        purpose = request.POST.get("purpose")
        note = request.POST.get("note")
        scheduled_at = request.POST.get("scheduled_at")

        Appointment.objects.create(patient_name=patient_name,patient_age=age,note=note,
                                   phone=phone,purpose=purpose,scheduled_at=scheduled_at)

        return redirect("/elders")
