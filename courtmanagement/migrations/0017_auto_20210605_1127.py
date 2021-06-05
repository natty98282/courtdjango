# Generated by Django 3.2 on 2021-06-05 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courtmanagement', '0016_auto_20210605_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(auto_created=True, default=123, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='UserAccount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]