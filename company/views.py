from django.shortcuts import render,redirect
from .forms import *
from .models import Company
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

def add_company(request):
    if request.method =='POST':
        form = CreateCompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            user = User.objects.get(pk=request.user.pk)
            user.has_company = True
            user.save()
            company.save()
            messages.success(request,'Company added successfully.')
            return redirect('dashboard:home')
        else:
            messages.warning(request,'Something went wrong. Please try again.')
            return redirect('company:add-company')
    else:
        form = CreateCompanyForm()
        return render(request,'company/add-company.html',{'form':form})
    
def update_company(request,slug):
    company = Company.objects.get(slug=slug)
    if request.method == 'POST':
        form = UpdateCompanyForm(request.POST,instance=company)
        if form.is_valid():
            form.save()
            messages.success(request,'Company info updated successfully.')
            return redirect('company:company-details',slug=company.slug)
        else:
            messages.warning(request,'Something went wrong. Try again')
            return redirect('company:company-details',slug=company.slug)
    else:
        form = UpdateCompanyForm(instance=company)
        return render(request,'company/update-company.html',{'form':form})
    
def company_details(request,slug):
    company = Company.objects.get(slug=slug)
    jobs = company.jobs.filter(status='Active').order_by('?')[:3]
    return render(request,'company/company-details.html',{'company':company,'jobs':jobs})


