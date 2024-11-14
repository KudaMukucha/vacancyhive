from django.urls import path
from .import views

app_name = 'company'

urlpatterns =[
    path('add-company/',views.add_company,name='add-company'),
    path('update-company/<slug:slug>/',views.update_company,name='update-company'),
    path('company-details/<slug:slug>/',views.company_details,name='company-details')
]