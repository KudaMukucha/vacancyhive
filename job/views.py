from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from company.models import Company
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .filters import JobFilter
from django.db.models import Q


User = get_user_model()

def create_job(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            company = Company.objects.get(pk = request.user.company.pk)
            job.company = company
            job.save()
            messages.success(request,'Job saved successfully. Please add other requirements.')
            return redirect('job:job-details',slug=job.slug)
        else:
            messages.warning(request,'Something went wrong. Try again')
            return redirect('job:create-job')
    else:
        form = CreateJobForm()
        return render(request,'job/create-job.html',{'form':form})
    
def update_job(request,slug):
    job = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST,instance=job)
        if form.is_valid():
            form.save()
            messages.success(request,'Job info updated successfully.')
            return redirect('job:job-details',slug=job.slug)
        else:
            messages.warning(request,'Something went wrong.Please try again')
            return redirect('job:job-details',slug=job.slug)
    else:
        form = UpdateJobForm(instance=job)
        return render(request,'job/update-job.html',{'form':form})
    
def delete_job(request,slug):
    job = Job.objects.get(slug=slug)
    job.delete()
    messages.success(request,'Job deleted successfully.')
    return redirect('job:jobs-per-company')

def jobs_per_company(request):
    company = Company.objects.get(slug=request.user.company.slug)
    jobs = company.jobs.all()
    return render(request,'job/jobs-per-company.html',{'jobs':jobs,'company':company})

def job_details(request,slug):
    job = Job.objects.get(slug=slug)
    company = Company.objects.get(slug = job.company.slug)
    company_jobs = company.jobs.filter(status='Active').order_by('?')[:3]
    responsibilities = job.responsibilities.all()
    experiences = job.experience.all()
    return render(request,'job/job-details.html',{'job':job,'company_jobs':company_jobs,'responsibilities':responsibilities,'experiences':experiences})

def add_job_responsibility(request,slug):
    job = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = AddJobResponsibility(request.POST)
        if form.is_valid():
            responsibility = form.save(commit=False)
            responsibility.job = job
            responsibility.save()
            messages.success(request,'New job responsibility added to job details')
            return redirect('job:add-job-responsibility',slug=job.slug)
        else:
            messages.warning(request,'Something went wrong. Please try again')
            return redirect('job:add-job-responsibility',slug=job.slug)
    else:
        form = AddJobResponsibility()
        return render(request,'job/add-job-responsibility.html',{'form':form,'job':job})
    

def add_job_experience(request,slug):
    job = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = AddJobExperience(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.job = job
            experience.save()
            messages.success(request,'New job experience added to job details')
            return redirect('job:add-job-experience',slug=job.slug)
        else:
            messages.warning(request,'Something went wrong. Please try again')
            return redirect('job:add-job-experience',slug=job.slug)
    else:
        form = AddJobExperience()
        return render(request,'job/add-job-experience.html',{'form':form,'job':job})
    
def delete_job_responsibility(request,pk):
    job_responsibility = JobResponsibility.objects.get(pk=pk)
    job = job_responsibility.job
    job_responsibility.delete()
    messages.success(request,'Job responsibility deleted successfully from job details.')
    return redirect('job:job-details',slug=job.slug)

def delete_job_experience(request,pk):
    job_experience = JobExperience.objects.get(pk=pk)
    job = job_experience.job
    job_experience.delete()
    messages.success(request,'Job experience deleted successfully from job details.')
    return redirect('job:job-details',slug=job.slug)

@login_required
def available_jobs(request):
    if request.user.is_authenticated:
        if request.user.is_candidate and request.user.has_resume:
            jobs_list = Job.objects.filter(status='Active').order_by('-created')
            
            paginator = Paginator(jobs_list,4)
            page_number = request.GET.get('page')

            try:
                jobs = paginator.page(page_number)
            except EmptyPage:
                jobs =  paginator.page(paginator.num_pages)
            except PageNotAnInteger:
                jobs = paginator.page(1)

            return render(request,'job/available-jobs.html',{'jobs':jobs})
        else:
            return redirect('dashboard:home')
    else:
        return render(request,'job/register-message.html')


def apply_to_job(request,slug):
    job = Job.objects.get(slug=slug)
    check_application = job.applications.filter(job=job,resume = request.user.resume).exists()

    if job.status == 'Active':
        if request.user.has_resume:
            if not check_application:
                JobApplication.objects.create(
                    job = job, resume = request.user.resume
                )
                messages.success(request,'You have successfully applied for this job!')
                return redirect('job:job-details',job.slug)
            else:
                messages.warning(request,'You have already applied to this job!')
                return redirect('job:job-details', job.slug)
        else:
            messages.warning(request,'You do not have a resume. Please create one to apply.')
            return redirect('job:job-details', job.slug)
    else:
        messages.warning(request,'Job no longer active.')
        return redirect('job:job-details', job.slug)
    
def delete_application(request,pk):
    application = JobApplication.objects.get(pk=pk)
    application.delete()
    messages.success(request,'You have deleted this job application.')
    return redirect('job:manage-applied-jobs')
    
def save_job(request,slug):
    job = Job.objects.get(slug=slug)
    check_saved = job.saved_jobs.filter(job=job,resume = request.user.resume).exists()

    if job.status == 'Active':
        if request.user.has_resume:
            if not check_saved:
                SaveJob.objects.create(
                    job = job, resume = request.user.resume
                )
                messages.success(request,'You have successfully saved this job!')
                return redirect('job:job-details',job.slug)
            else:
                messages.warning(request,'You have already saved this job!')
                return redirect('job:job-details', job.slug)
        else:
            messages.warning(request,'You do not have a resume. Please create one to save.')
            return redirect('job:job-details', job.slug)
    else:
        messages.warning(request,'Job no longer active.')
        return redirect('job:job-details', job.slug)
    
def saved_jobs(request):
    jobs = SaveJob.objects.filter(resume = request.user.resume)
    return render(request,'job/saved-jobs.html',{'jobs':jobs})

def delete_saved_job(request,pk):
    job = SaveJob.objects.get(pk=pk)
    job.delete()
    messages.success(request,'Job removed successfully')
    return redirect('job:all-saved-jobs')

def manage_applied_jobs(request):
    jobs = JobApplication.objects.filter(resume = request.user.resume)
    return render(request,'job/manage-applied-jobs.html',{'jobs':jobs})

def applicants_per_job(request,pk):
    job = Job.objects.get(pk=pk)
    applicants = job.applications.all()
    accepted_applicants = job.applications.filter(status = 'Accepted')
    declined_applicants = applicants.filter(status = 'Declined')
    return render(request,'job/applicants-per-job.html',{'job':job,'applicants':applicants,'approved':accepted_applicants,'declined':declined_applicants})

def accept_application(request,pk):
    application = JobApplication.objects.get(pk=pk)
    application.status = 'Accepted'
    application.save()
    messages.success(request,'You have accepted this candidate')
    return redirect('job:applicants-per-job',pk = application.job.pk)

def reject_application(request,pk):
    application = JobApplication.objects.get(pk=pk)
    application.status = 'Declined'
    application.save()
    messages.success(request,'You have declined this candidate')
    return redirect('job:applicants-per-job',pk = application.job.pk)


def search_jobs(request):
    query = request.GET.get('q')
    jobs = Job.objects.filter(status='Active')

    if query:
        jobs = jobs.filter(
            Q(title__icontains = query) |
            Q(description__icontains=query) |
             Q(company__name__icontains=query)

        )
    jobs = jobs.order_by('title') 
    
    paginator = Paginator(jobs,4)
    page_number = request.GET.get('page',1)
    

    try:
        jobs = paginator.page(page_number)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    page_number = request.GET.get('page',1)
    return render(request,'job/search-results.html',{'jobs':jobs,'query':query})