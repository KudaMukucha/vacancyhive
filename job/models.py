from django.db import models
from django.contrib.auth import get_user_model
from company.models import Company
from django.utils.text import slugify
from django.utils import timezone
from resume.models import Resume

User = get_user_model()

class JobCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

class Job(models.Model):
    PAY_MODE_CHOICES=[
        ('Hourly','Hourly'),
        ('Daily','Daily'),
        ('Weekly','Weekly'),
        ('Monthly','Monthly')
    ]
    JOB_TYPE_CHOICES =[
        ('Part Time','Part Time'),
        ('Full Time','Full Time'),
        ('Freelance','Freelance'),
        ('Temporary','Temporary'),
        ('Internship','Internship'),
        ('Contract','Contract')
    ]
    LOCATION_CHOICES =[
        ('Remote','Remote'),
        ('Hybrid','Hybrid'),
        ('Onsite','Onsite')
    ]
    STATUS_CHOICES =[
        ('Pending','Pending'),
        ('Active','Active'),
        ('Expired','Expired')
    ]
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='jobs')
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(blank=True,null=True)
    updated = models.DateField(blank=True,null=True)
    salary = models.PositiveIntegerField()
    pay_mode = models.CharField(max_length=100,choices=PAY_MODE_CHOICES)
    job_type = models.CharField(max_length=50,choices=JOB_TYPE_CHOICES)
    location = models.CharField(max_length=50,choices=LOCATION_CHOICES)
    category = models.ForeignKey(JobCategory,on_delete=models.CASCADE,related_name='jobs')
    expiry = models.DateTimeField(null=True)
    hours_per_week = models.PositiveIntegerField()
    description = models.TextField()
    published = models.BooleanField(default=False)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.created is None:
            self.created = timezone.localtime(timezone.now())
        self.updated = timezone.localtime(timezone.now())
        super().save(*args,**kwargs)

class JobResponsibility(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='responsibilities')
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class JobExperience(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='experience')
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class JobApplication(models.Model):
    APPLICATION_STATUS =[
        ('Pending','Pending'),
        ('Accepted','Accepted'),
        ('Declined','Declined')
    ]
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='applications')
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='applications')
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices=APPLICATION_STATUS,default='Pending')

    def __str__(self):
        return self.job.title

class SaveJob(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='saved_jobs')
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='saved_jobs')
    saved_on = models.DateTimeField(auto_now_add=True)




