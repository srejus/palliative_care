from django.shortcuts import render,redirect
from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from accounts.models import Account
from .models import *
from hospital.models import Emergency


# Create your views here.
@method_decorator(login_required,name='dispatch')
class CareWorkerView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        if acc.user_type != Account.CARE_WORKER:
            msg = "You don't have permission to access this page!"
            return redirect(f"/?msg={msg}")
        
        return render(request,'cw_home.html')


@method_decorator(login_required,name='dispatch')
class CwhiringReqView(View):
    def get(self,request):
        reqs = RequestCwHiring.objects.filter(cw__user__user=request.user)
        return render(request,'cw_view_hiring_req.html',{'reqs':reqs})
    

@method_decorator(login_required,name='dispatch')
class CwEmergencyReqView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        elder = Account.objects.filter(care_worker_id=acc.id)
        if elder.exists():
            elder = elder.last()
            reqs = Emergency.objects.filter(user=elder)
        else:
            reqs = []
        return render(request,'cw_view_emergency_req.html',{'reqs':reqs})


@method_decorator(login_required,name='dispatch')
class CwAcceptReqView(View):
    def get(self,request,id):
        RequestCwHiring.objects.filter(id=id).update(status='ACCEPTED')
        return redirect("/care-worker/hiring-requests")
    

@method_decorator(login_required,name='dispatch')
class CwRejectReqView(View):
    def get(self,request,id):
        RequestCwHiring.objects.filter(id=id).update(status='REJECTED')
        return redirect("/care-worker/hiring-requests")