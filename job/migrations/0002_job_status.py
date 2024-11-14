# Generated by Django 4.2.7 on 2024-10-29 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Active', 'Active'), ('Expired', 'Expired')], default='Pending', max_length=50),
        ),
    ]