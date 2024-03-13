from django.shortcuts import render,redirect
from django.views import View

from accounts.models import Account

# Create your views here.
class IndexView(View):
    def get(self,request):
        msg = request.GET.get("msg")
        if request.user.is_authenticated:
            acc = Account.objects.get(user=request.user)
            if acc.user_type == Account.ELDER:
                return redirect("/elders/")
            if acc.user_type ==  Account.CARE_WORKER:
                return redirect("/care-worker/")
            if acc.user_type == Account.HEALTH_WORKER:
                return redirect("/health-worker/")
            
        return render(request,'index.html',{'msg':msg})