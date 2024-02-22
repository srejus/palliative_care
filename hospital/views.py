from django.shortcuts import render,redirect
from django.views import View

# Create your views here.
class EmergencyView(View):
    def get(self,request):
        msg = "Emergency Requested!"
        return redirect(f"/?msg={msg}")