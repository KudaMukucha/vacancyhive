from django import forms
from .models import *

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude =['company','published','expiry','slug','created','updated','status']


class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude =['company','published','expiry','slug','created','updated']

class AddJobResponsibility(forms.ModelForm):
    class Meta:
        model = JobResponsibility
        fields = ['name']


class AddJobExperience(forms.ModelForm):
    class Meta:
        model = JobExperience
        fields = ['name']