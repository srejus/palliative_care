from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *
from accounts.models import Account
from hospital.models import Emergency

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
        
        reqs = RequestHwHiring.objects.filter(hw__user__user=request.user)
        return render(request,'hw_view_hiring_req.html',{'reqs':reqs}) 
        

        

@method_decorator(login_required,name='dispatch')
class HwAcceptReqView(View):
    def get(self,request,id):
        RequestHwHiring.objects.filter(id=id).update(status='ACCEPTED')
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