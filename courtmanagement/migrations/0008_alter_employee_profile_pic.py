# Generated by Django 3.2 on 2021-05-31 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courtmanagement', '0007_alter_employee_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profileimage/'),
        ),
    ]