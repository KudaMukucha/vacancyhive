from django import forms
from .models import *

class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude =['user','slug','created','updated']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['founded_in'].widget.attrs['placeholder'] = 'Select Date'
        self.fields['primary_industry'].empty_label = 'Select Primary Industry'

class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude =['user','slug','created','updated']

