from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

def add_resume(request):
    if request.method == 'POST':
        form = AddResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            user = User.objects.get(pk=request.user.pk)
            user.has_resume = True
            user.save()
            resume.save()
            messages.success(request,'You have just added your resume.')
            return redirect('resume:resume-details',pk=resume.pk)
        else:
            messages.warning(request,'Something went wrong.Try again.')
            return redirect('resume:add-resume')
    else:
        form = AddResumeForm()
        return render(request,'resume/add-resume.html',{'form':form})
    
def update_resume(request,pk):
    resume = Resume.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateResumeForm(request.POST,instance=resume)
        if form.is_valid():
            form.save()
            messages.success(request,'Resume information updated successfully.')
            return redirect('resume:resume-details',pk=resume.pk)
        else:
            messages.warning(request,'Something went wrong.Please try again.')
            return redirect('resume:update-resume',pk=resume.pk)
    else:
        form = UpdateResumeForm(instance=resume)
        return render(request,'resume/update-resume.html',{'form':form,'resume':resume})
    
def resume_details(request,pk):
    resume = Resume.objects.get(pk=pk)
    educations = resume.education.all().order_by('-end_date')
    experiences = resume.work_experience.all().order_by('-end_date')
    return render(request,'resume/resume-details.html',{'resume':resume,'educations':educations,'experiences':experiences})

def add_education(request,pk):
    resume = Resume.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddEducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.resume = resume 
            education.save()
            messages.success(request,'Education added to resume successfully.')
            return redirect('resume:add-education',pk=resume.pk)
        else:
            messages.warning(request,'Something went wrong. Try again.')
            return redirect('resume:add-education',pk=resume.pk)
    else:
        form = AddEducationForm()
        return render(request,'resume/add-education.html',{'form':form,'resume':resume})
    
def update_education(request,pk):
    education = Education.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateEducationForm(request.POST,instance=education)
        if form.is_valid():
            form.save()
            messages.success(request,'Education information updated succesfully.')
            return redirect('resume:resume-details',pk=education.resume.pk)
        else:
            messages.warning(request,'Something went wrong. Try again.')
            return redirect('resume:update-education',pk=education.pk)
    else:
        form = UpdateEducationForm(instance=education)
        return render(request,'resume/update-education.html',{'form':form})
    
def delete_education(request,pk):
    education = Education.objects.get(pk=pk)
    resume = Resume.objects.get(pk=education.resume.pk)
    education.delete()
    messages.success(request,'Education information deleted successfully.')
    return redirect('resume:resume-details',pk=resume.pk)
    

def add_work_experience(request,pk):
    resume = Resume.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddWorkExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.resume = resume 
            experience.save()
            messages.success(request,'Work experience added to resume successfully.')
            return redirect('resume:add-experience',pk=resume.pk)
        else:
            messages.warning(request,'Something went wrong. Try again.')
            return redirect('resume:add-experience',pk=resume.pk)
    else:
        form = AddWorkExperienceForm()
        return render(request,'resume/add-work-experience.html',{'form':form,'resume':resume})
    
def update_work_experience(request,pk):
    experience = WorkExperience.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateWorkExperienceForm(request.POST,instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request,'Work experience information updated succesfully.')
            return redirect('resume:resume-details',pk=experience.resume.pk)
        else:
            messages.warning(request,'Something went wrong. Try again.')
            return redirect('resume:update-experience',pk=experience.pk)
    else:
        form = UpdateWorkExperienceForm(instance=experience)
        return render(request,'resume/update-work-experience.html',{'form':form})
    
def delete_work_experience(request,pk):
    experience = WorkExperience.objects.get(pk=pk)
    resume = Resume.objects.get(pk=experience.resume.pk)
    experience.delete()
    messages.success(request,'Work Experience information deleted successfully.')
    return redirect('resume:resume-details',pk=resume.pk)

         


