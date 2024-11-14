from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.
User = get_user_model()

class Company(models.Model):
    PROVINCE_CHOICES =[
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
    PRIMARY_INDUSTRY_CHOICES =[
    ('Software', 'Software'),
    ('Finance', 'Finance'),
    ('Healthcare', 'Healthcare'),
    ('Manufacturing', 'Manufacturing'),
    ('Retail', 'Retail'),
    ('Construction', 'Construction'),
    ('Education', 'Education'),
    ('Transportation', 'Transportation')
    ]
    COMPANY_SIZE_CHOICES =[
    ('1-10', '1-10'),
    ('11-50', '11-50'),
    ('51-200', '51-200'),
    ('201-500', '201-500'),
    ('501-1000', '501-1000'),
    ('1000+', '1000+')
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='company')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    logo = models.ImageField(blank=True,null=True,upload_to='logos')
    province = models.CharField(max_length=100,choices=PROVINCE_CHOICES)
    country = models.CharField(max_length=100,choices=[('Zimbabwe', 'Zimbabwe')])
    primary_industry = models.CharField(max_length=100,choices=PRIMARY_INDUSTRY_CHOICES)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    company_size = models.CharField(max_length=20,choices=COMPANY_SIZE_CHOICES)
    founded_in = models.DateField()
    location = models.CharField(max_length=100)
    linkedin = models.URLField()
    website = models.URLField()
    description = models.TextField()
    created = models.DateTimeField(blank=True,null=True)
    updated = models.DateTimeField(blank=True,null=True)


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.created is None:
            self.created = timezone.localtime(timezone.now())
        self.updated = timezone.localtime(timezone.now())
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name