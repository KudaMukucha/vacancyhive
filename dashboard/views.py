from datetime import datetime
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.user.is_recruiter:
        current_year = datetime.now().year
        return render(request,'dashboard/recruiter-dashboard.html',{'current_year':current_year})
    elif request.user.is_candidate:
        current_year = datetime.now().year
        return render(request,'dashboard/candidate-dashboard.html',{'current_year':current_year})
