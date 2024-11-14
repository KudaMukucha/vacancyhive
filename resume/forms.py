from django import forms
from .models import *

class AddResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ['user','created','updated']
    

class UpdateResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ['user','created','updated']

class AddEducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ['resume']


class UpdateEducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ['resume']


class AddWorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        exclude = ['resume']

class UpdateWorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        exclude = ['resume']