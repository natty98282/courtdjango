# Generated by Django 3.2 on 2021-06-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courtmanagement', '0014_alter_case_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='casefile',
            field=models.FileField(default=123, upload_to='casefile/'),
            preserve_default=False,
        ),
    ]