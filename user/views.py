from user import forms
from user.forms import CustomerRegistrationForm,ProfileForm,AdderssForm
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from user.models import Adderss, UserProfile
from django.contrib import messages
from django.views import View
# Create your views here.
def dashbord(request):
    profile=UserProfile.objects.filter(user=request.user)
    return render(request,"users/dashbord.html",{'profile':profile})



def edit_profile(request):
    
    if request.method =="GET":
        form = ProfileForm()
        return render(request,'profile\edit_profile.html',{'form':form})
    else:
        if request.method =="POST":
            form = ProfileForm(request.POST)
            if form.is_valid():
                usr =request.user
                 
                name =form.cleaned_data['name']
                
                img=form.cleaned_data['img']
                DOB =form.cleaned_data['DOB']
                gender =form.cleaned_data['gender']
                phone =form.cleaned_data['phone']

                reg=UserProfile(user=usr,name=name,DOB=DOB,
                phone=phone,gender=gender,img=img)
                reg.save()
            messages.success(request, 'Your profile updated successfully!') 
        return render(request, 'profile\edit_profile.html',{'form':form}) 



def add_adderss(request):
    if request.method =="GET":
        form = AdderssForm()
        return render(request,"profile/add_adderss.html",{'form':form,
        'active':'btn-primary'})
    else:
        if request.method =="POST":
            form = AdderssForm(request.POST)
            if form.is_valid():
                usr =request.user
                 
                state =form.cleaned_data['state']
                
                zipcode=form.cleaned_data['zipcode']
                city =form.cleaned_data['city']
                add =form.cleaned_data['add']
                
                reg=Adderss(user=usr,city=city,state=state,
                add=add,zipcode=zipcode)
                reg.save()
            messages.success(request, 'Your profile updated successfully!')     
            return render(request,"profile/add_adderss.html",{'form':form,'active':'btn-primary'})
                                        


    
         


#class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'users/customerregistration.html',{"form":form})
    def post(self,request):
         form=CustomerRegistrationForm(request.POST)
         if form.is_valid():
             form.save()
             return render(request,'users/customerregistration.html',{"form":form})        


def CustomerRegistrationView(request):
    if  request.method =="GET":
        form=CustomerRegistrationForm()
        return render(request,'users/customerregistration.html',{"form":form})
    else:
        if request.method =="POST":
            form=CustomerRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                 
    messages.success(request, 'Your account created successfully!') 
                
    return render(request,'users/customerregistration.html',{"form":form})  















def address(request):
    add=Adderss.objects.filter(user=request.user)
    return render (request,'profile/address.html',{'add':add})