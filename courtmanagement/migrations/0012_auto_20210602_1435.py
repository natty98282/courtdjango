# Generated by Django 3.2 on 2021-06-02 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courtmanagement', '0011_case_qr_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Prisoner_Registration',
        ),
        migrations.AlterField(
            model_name='employee',
            name='UserAccount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='manager',
            name='UserAccount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]