from user import forms
from user.forms import CustomerRegistrationForm,ProfileForm
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from user.models import UserProfile
from django.contrib import messages
from django.views import View
# Create your views here.
def dashbord(request):
    return render(request,"users/dashbord.html")



def show_profile(request):
    profile=UserProfile.objects.all()

    return render(request,"profile/show_profile.html",{"pro":profile})



def edit_profile(request):
    if request.method =="GET":
        form = ProfileForm()
        return render(request,"profile/edit_profile.html",{'form':form,
        'active':'btn-primary'})
    else:
        if request.method =="POST":
            form = ProfileForm(request.POST)
            if form.is_valid():
                usr =request.user
                name =form.cleaned_data['name'] 
                state =form.cleaned_data['state']
                DOB =form.cleaned_data['DOB']
                gender =form.cleaned_data['gender']
                city =form.cleaned_data['city']
                add =form.cleaned_data['add']
                phone =form.cleaned_data['phone']
                reg=UserProfile(user=usr,name=name,city=city,DOB=DOB,state=state,
                gender=gender,phone=phone,add=add)
                reg.save()
            messages.success(request, 'Your profile updated successfully!')     
            return render(request,"profile/edit_profile.html",{'form':form,
                           'active':'btn-primary'})
                                        


    
         


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
    add=UserProfile.objects.filter(user=request.user)
    return render (request,'profile/address.html',{'add':add})