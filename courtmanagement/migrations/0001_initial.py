# Generated by Django 3.2 on 2021-05-28 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=45)),
                ('Last_Name', models.CharField(max_length=45)),
                ('CaseType', models.CharField(max_length=45)),
                ('Address', models.CharField(max_length=45)),
                ('phone_no', models.CharField(max_length=45)),
                ('Status', models.CharField(max_length=45)),
                ('Age', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Name', models.CharField(max_length=255)),
                ('Writte_Comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_Id', models.CharField(max_length=45)),
                ('First_Name', models.CharField(max_length=45)),
                ('Last_Name', models.CharField(max_length=45)),
                ('Address', models.CharField(max_length=45)),
                ('phone_no', models.CharField(max_length=45)),
                ('Sallary', models.CharField(max_length=45)),
                ('Status', models.CharField(max_length=45)),
                ('Age', models.CharField(max_length=45)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Judge_id', models.CharField(max_length=45)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courtmanagement.employee')),
            ],
        ),
        migrations.CreateModel(
            name='LowOfficer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officer_id', models.CharField(max_length=45)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courtmanagement.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Prisoner_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('crime', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('room_number', models.IntegerField()),
                ('Punishment', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45)),
                ('Password', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Summon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Summon_body', models.TextField()),
                ('Judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courtmanagement.judge')),
                ('LowOfficer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courtmanagement.lowofficer')),
            ],
        ),
        migrations.CreateModel(
            name='Shedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now=True)),
                ('Court_Room', models.IntegerField()),
                ('body', models.TextField()),
                ('Case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courtmanagement.case')),
                ('Judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courtmanagement.judge')),
                ('LowOfficer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courtmanagement.lowofficer')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=45)),
                ('Last_Name', models.CharField(max_length=45)),
                ('Address', models.CharField(max_length=45)),
                ('phone_no', models.CharField(max_length=45)),
                ('UserAccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courtmanagement.useraccount')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='UserAccount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courtmanagement.useraccount'),
        ),
        migrations.CreateModel(
            name='Decision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Writte_Dession', models.TextField()),
                ('Date', models.DateTimeField(auto_now=True)),
                ('Case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courtmanagement.case')),
                ('Judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courtmanagement.judge')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='Judge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courtmanagement.judge'),
        ),
        migrations.AddField(
            model_name='case',
            name='LowOfficer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courtmanagement.lowofficer'),
        ),
    ]
