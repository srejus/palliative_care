from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *
from accounts.models import Account
from hospital.models import Emergency,Appointment
from elders.models import HealthRecord

# Create your views here.
@method_decorator(login_required,name='dispatch')
class HwHomeView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        if acc.user_type != Account.HEALTH_WORKER:
            msg = "You don't have access to this page"
            return redirect(f"/?msg={msg}")
        
        return render(request,'hw_home.html')
    

@method_decorator(login_required,name='dispatch')
class HwHiringReqView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        if acc.user_type != Account.HEALTH_WORKER:
            msg = "You don't have access to this page"
            return redirect(f"/?msg={msg}")
        
        reqs = RequestHwHiring.objects.filter(hw__user__user=request.user,status='SENT')
        return render(request,'hw_view_hiring_req.html',{'reqs':reqs}) 
        

@method_decorator(login_required,name='dispatch')
class HwAcceptReqView(View):
    def get(self,request,id):
        RequestHwHiring.objects.filter(id=id).update(status='ACCEPTED')
        req = RequestHwHiring.objects.filter(id=id).last()
        Account.objects.filter(user__user=req.user).update(medical_worker_id=Account.objects.get(user=request.user).id)
        return redirect("/health-worker/hiring-requests")
    

@method_decorator(login_required,name='dispatch')
class HwRejectReqView(View):
    def get(self,request,id):
        RequestHwHiring.objects.filter(id=id).update(status='REJECTED')
        return redirect("/health-worker/hiring-requests")
    

@method_decorator(login_required,name='dispatch')
class HwManageEmergencyView(View):
    def get(self,request):
        reqs = Emergency.objects.all().order_by('-id')
        return render(request,'hw_manage_emergency.html',{'reqs':reqs})
    

@method_decorator(login_required,name='dispatch')
class HwManageHealthReportView(View):
    def get(self,request):
        msg = request.GET.get("msg")
        records = HealthRecord.objects.filter(created_by__user=request.user).order_by('-id')
        return render(request,'hw_manage_healthreport.html',{'records':records,'msg':msg})
    

@method_decorator(login_required,name='dispatch')
class HwAddHealthReportView(View):
    def get(self,request):
        elders = Account.objects.filter(medical_worker_id=Account.objects.get(user=request.user).id)
        if not elders.exists():
            msg = "No elders found for Create Record!"
            return redirect(f"/health-worker/manage-health-report?msg={msg}")
        return render(request,'hw_create_health_report.html',{'elders':elders})
    
    def post(self,request):
        elder_id = request.POST.get("elder")
        sugar = request.POST.get("sugar")
        pressure = request.POST.get("pressure")
        weight = request.POST.get("weight")
        col = request.POST.get("col")
        notes = request.POST.get("notes")
        
        elder = Account.objects.get(id=elder_id)
        acc = Account.objects.get(user=request.user)

        HealthRecord.objects.create(elder=elder,created_by=acc,sugar=sugar,
                                    cholesterol=col,weight=weight,pressure=pressure,notes=notes)

        return redirect("/health-worker/manage-health-report")
    

@method_decorator(login_required,name='dispatch')
class HwDeleteRecordView(View):
    def get(self,request,id):
        HealthRecord.objects.filter(id=id).delete()
        msg = "Record deleted successfully!"
        return redirect(f"/health-worker/manage-health-report?msg={msg}")
    

@method_decorator(login_required,name='dispatch')
class HwManageAppointmentView(View):
    def get(self,request):
        appointments = Appointment.objects.filter(hw__user__user=request.user).order_by('-id')
        return render(request,'hw_appointments.html',{'appointments':appointments})
    


@method_decorator(login_required,name='dispatch')
class HwAcceptAppointmentView(View):
    def get(self,request,id):
        Appointment.objects.filter(id=id).update(status='ACCEPTED')
        return redirect("/health-worker/manage-appointments")
    


@method_decorator(login_required,name='dispatch')
class HwRejectAppointmentView(View):
    def get(self,request,id):
        Appointment.objects.filter(id=id).update(status='REJECTED')
        return redirect("/health-worker/manage-appointments")