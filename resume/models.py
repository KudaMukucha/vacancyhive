from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Resume(models.Model):
    PROVINCE_CHOICES = [
        ('Harare', 'Harare'),
        ('Bulawayo', 'Bulawayo'),
        ('Manicaland', 'Manicaland'),
        ('Mashonaland East', 'Mashonaland East'),
        ('Mashonaland Central', 'Mashonaland Central'),
        ('Mashonaland West', 'Mashonaland West'),
        ('Masvingo', 'Masvingo'),
        ('Midlands', 'Midlands'),
        ('Matabeleland North', 'Matabeleland North'),
        ('Matabeleland South', 'Matabeleland South')
    ]
    
    EXPERIENCE_CHOICES = [
        ('0 - 2', '0 - 2 years'),
        ('2 - 5', '2 - 5 years'),
        ('5 - 10', '5 - 10 years'),
        ('10+', '10+ years')
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    
    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Shona', 'Shona'),
        ('Ndebele', 'Ndebele')
    ]
    
    EDUCATIONAL_LEVEL_CHOICES = [
        ('None', 'None'),
        ('O Level', 'O Level'),
        ('Diploma', 'Diploma'),
        ('Bachelors', 'Bachelor\'s Degree'),
        ('Masters', 'Master\'s Degree'),
        ('Doctorate', 'Doctorate Degree')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resume')
    province = models.CharField(max_length=100, choices=PROVINCE_CHOICES)
    country = models.CharField(max_length=100, choices=[('Zimbabwe', 'Zimbabwe')])
    experience = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)  # Reduced max_length
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES)
    phone = models.CharField(max_length=20,null=True)
    education_level = models.CharField(max_length=100, choices=EDUCATIONAL_LEVEL_CHOICES)
    linkedin = models.URLField()
    twitter = models.URLField()
    about = models.TextField()
    video_link = models.URLField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Education(models.Model):
    DEGREE_TYPE_CHOICES = [
        ('Bachelors', 'Bachelor\'s Degree'),
        ('Masters', 'Master\'s Degree'),
        ('Doctorate', 'Doctorate Degree')
    ]
    
    STILL_SCHOOLING_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education')
    degree_type = models.CharField(max_length=100, choices=DEGREE_TYPE_CHOICES)
    course = models.CharField(max_length=255)
    institution = models.CharField(max_length=255,null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500)
    still_schooling = models.CharField(max_length=3, choices=STILL_SCHOOLING_CHOICES, default='No')

class WorkExperience(models.Model):
    STILL_WORKING_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='work_experience')
    role = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    still_working = models.CharField(max_length=3, choices=STILL_WORKING_CHOICES, default='No')
    description = models.CharField(max_length=500,null=True)