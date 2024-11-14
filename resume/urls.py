from django.urls import path
from .import views

app_name ='resume'

urlpatterns =[
    path('add-resume/',views.add_resume,name='add-resume'),
    path('update-resume/<int:pk>/',views.update_resume,name='update-resume'),
    path('resume-details/<int:pk>/',views.resume_details,name='resume-details'),

    path('add-education/<int:pk>/',views.add_education,name='add-education'),
    path('update-education/<int:pk>/',views.update_education,name='update-education'),
    path('delete-education/<int:pk>/',views.delete_education,name='delete-education'),
    
    path('add-work-experience/<int:pk>/',views.add_work_experience,name='add-experience'),
    path('update-work-experience/<int:pk>/',views.update_work_experience,name='update-experience'),
    path('delete-work-experience/<int:pk>/',views.delete_work_experience,name='delete-experience')
]