from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse

from care_worker.models import CareWorker
from hospital.models import Appointment


# Create your views here.
@method_decorator(login_required, name='dispatch')
class ElderHomeView(View):
    def get(self,request):
        return render(request,'elders/elder_home.html')
    

@method_decorator(login_required, name='dispatch')
class FindCareWorkerView(View):
    def get(self,request,id=None):
        care_workers = CareWorker.objects.filter(is_approved=True)
        if id:
            worker = care_workers.get(id=id)
            return render(request,'elders/care_worker_details.html',{'worker':worker})
        return render(request,'elders/find_care_worker.html',{'care_workers':care_workers})
    

@method_decorator(login_required, name='dispatch')
class SendHiringRequestToCareWorkerView(View):
    def get(self,request,id):
        print("----Sending Request to Hiring Care Worker-------")
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
