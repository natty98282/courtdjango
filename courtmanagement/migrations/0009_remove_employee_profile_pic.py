# Generated by Django 3.2 on 2021-06-01 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courtmanagement', '0008_alter_employee_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='profile_pic',
        ),
    ]