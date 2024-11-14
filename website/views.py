from django.shortcuts import render,redirect
from datetime import datetime
from job.models import Job
# Create your views here.
def home(request):
    current_year = datetime.now().year
    all_jobs = Job.objects.filter(status='Active')
    jobs = Job.objects.filter(status='Active').order_by('?')[:6]
    return render(request,'website/home.html',{'current_year':current_year,'jobs':jobs,'all_jobs':all_jobs})

def about(request):
    return render(request,'website/about.html')

def contact(request):
    return render(request,'website/contact.html')