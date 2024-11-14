# Generated by Django 4.2.7 on 2024-10-28 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateField(blank=True, null=True)),
                ('salary', models.PositiveIntegerField()),
                ('pay_mode', models.CharField(choices=[('Hourly', 'Hourly'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=100)),
                ('job_type', models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Freelance', 'Freelance'), ('Temporary', 'Temporary'), ('Internship', 'Internship'), ('Contract', 'Contract')], max_length=50)),
                ('location', models.CharField(choices=[('Remote', 'Remote'), ('Hybrid', 'Hybrid'), ('Onsite', 'Onsite')], max_length=50)),
                ('expiry', models.DateTimeField(null=True)),
                ('hours_per_week', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobResponsibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsibilities', to='job.job')),
            ],
        ),
        migrations.CreateModel(
            name='JobExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='job.job')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='job.jobcategory'),
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='company.company'),
        ),
    ]
