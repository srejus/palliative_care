from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *
from care_worker.models import CareWorker
from medical_worker.models import MedicalWorker

# Create your views here.

class LoginView(View):
    def get(self,request):
        err = request.GET.get("err")
        return render(request,'login.html',{'err':err})

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        next = request.GET.get("next","/")

        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next)
        err = "Invalid credentails!"
        return redirect(f"/account/login/?err={err}")
    

class SignupView(View):
    def get(self,request):
        err = request.GET.get("err")
        return render(request,'signup.html',{'err':err})
    
    def post(self,request):
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        full_name = request.POST.get("fullname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        place = request.POST.get("place")
        address = request.POST.get("address")
        user_type = request.POST.get("user_type")
        age = request.POST.get("age")

        # exp = request.POST.get("exp")
        # if exp == '':
        #     exp = 0

        if password1 != password2:
            err = "Password not matching!"
            return redirect(f"/accounts/signup?err={err}")
    
        user = User.objects.filter(username=username)
        if user.exists():
            err = "User with this username already exists"
            return redirect(f"/accounts/signup?err={err}")
        
        acc = Account.objects.filter(Q(email=email) | Q(phone=phone)).exists()
        if acc:
            err = "User with this phone or email already exists"
            return redirect(f"/accounts/signup?err={err}")
        
        user = User.objects.create_user(username=username,email=email,password=password1)
        acc = Account.objects.create(user=user,full_name=full_name,phone=phone,
                                     email=email,address=address,place=place,user_type=user_type)
        
        if user_type == 'CARE_WORKER':
            CareWorker.objects.create(user=acc,full_name=full_name,
                                      phone=phone,email=email,age=age,place=place)
        elif user_type == 'HEALTH_WORKER':
            MedicalWorker.objects.create(user=acc,full_name=full_name,
                                         phone=phone,email=email,place=place)

        return redirect('/accounts/login/')
        

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        return render(request,'profile.html',{'acc':acc})
    

@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        return render(request,'edit_profile.html',{'acc':acc})
    
    def post(self,request):
        full_name = request.POST.get("fullname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        place = request.POST.get("place")
        address = request.POST.get("address")

        acc = Account.objects.get(user=request.user)
        acc.full_name = full_name
        acc.email = email
        acc.place = place
        acc.address = address
        acc.phone = phone
        acc.save()
        return redirect("/accounts/profile")
    

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("/accounts/login/")