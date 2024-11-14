from django.urls import path
from .import views

app_name ='accounts'

urlpatterns =[
    path('register-candidate/',views.register_candidate,name='register-candidate'),
    path('register-recruiter/',views.register_recruiter,name='register-recruiter'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('change-password/',views.change_password,name='change-password'),
    path('update-profile/<int:pk>/',views.update_profile,name='update-profile')
]