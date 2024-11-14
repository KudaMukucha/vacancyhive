from django.urls import path
from .import views

app_name = 'job'

urlpatterns =[
    path('create-job/',views.create_job,name='create-job'),
    path('update-job/<slug:slug>/',views.update_job,name='update-job'),
    path('delete-job/<slug:slug>/',views.delete_job,name='delete-job'),
    path('jobs-per-company/',views.jobs_per_company,name='jobs-per-company'),
    path('job-details/<slug:slug>/',views.job_details,name='job-details'),
    path('add-job-responsibility/<slug:slug>/',views.add_job_responsibility,name='add-job-responsibility'),
    path('add-job-experience/<slug:slug>/',views.add_job_experience,name='add-job-experience'),
    
    path('delete-job-responsibility/<int:pk>/',views.delete_job_responsibility,name='delete-job-responsibility'),
    path('delete-job-experience/<int:pk>/',views.delete_job_experience,name='delete-job-experience'),

    path('available-jobs/',views.available_jobs,name='available-jobs'),

    path('apply-job/<slug:slug>/',views.apply_to_job,name='apply-job'),
    path('save-job/<slug:slug>/',views.save_job,name='save-job'),

    path('manage-applied-jobs/',views.manage_applied_jobs,name='manage-applied-jobs'),
    path('delete-application/<int:pk>/',views.delete_application,name='delete-application'),

    path('applicants-per-job/<int:pk>/',views.applicants_per_job,name='applicants-per-job'),

    path('accept-application/<int:pk>/',views.accept_application,name='accept-application'),
    path('reject-application/<int:pk>/',views.reject_application,name='reject-application'),
    path('all-saved-jobs/',views.saved_jobs,name='all-saved-jobs'),
    path('delete-saved-job/<int:pk>/',views.delete_saved_job,name='delete-saved-job'),

    path('search/',views.search_jobs,name='search-jobs')

]