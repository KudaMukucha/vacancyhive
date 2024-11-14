from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.contrib import messages

# Create your views here.
User = get_user_model()

def register_candidate(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_candidate = True
            user.username = user.email
            user.save()
            messages.success(request,'Account created successfully. Please login')
            return redirect('accounts:login')
        else:
            messages.warning(request,'Oops,something went wrong. Try again')
            return redirect('accounts:register-candidate')
    else:
        form = RegisterUserForm()
        return render(request,'accounts/register-candidate.html',{'form':form})

def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_recruiter = True
            user.username = user.email
            user.save()
            messages.success(request,'Account created successfully. Please login')
            return redirect('accounts:login')
        else:
            messages.warning(request,'Oops,something went wrong. Please try again.')
            return redirect('accounts:register-recruiter')
    else:
        form = RegisterUserForm(request.POST)
        return render(request,'accounts/register-recruiter.html',{'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user is not None and user.is_active:
            login(request,user)
            return redirect('dashboard:home')
        else:
            messages.warning(request,'Oops,something went wrong. Try again')
            return redirect('accounts:login')
    else:
        return render(request,'accounts/login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request,'You are now logged out.')
    return redirect('accounts:login')

def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password updated successfully.')
            return redirect('dashboard:home')
        else:
            messages.warning(request,'Oops,something went wrong. Please try again.')
    else:
        form = UserPasswordChangeForm(request.user)
        return render(request,'accounts/change-password.html',{'form':form})

def update_profile(request,pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateProfile(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Your profile information has been updated')
            return redirect('accounts:update-profile',pk = user.pk)
        else:
            messages.warning(request,'Oops,something went wrong. Try again')
            return redirect('accounts:update-profile',pk=user.pk)
    else:
        form = UpdateProfile(instance=user)
        return render(request,'accounts/update-profile.html',{'form':form})        
