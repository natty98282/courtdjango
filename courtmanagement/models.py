from django.db import models
import qrcode
from django import forms
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.

 

class Manager(models.Model):
    UserAccount = models.ForeignKey(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=45)
    Last_Name = models.CharField(max_length=45)
    Address = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=45)
    
    def __str__(self):
      return self.First_Name + '|' + str(self.Last_Name)       

class Employee(models.Model):
    UserAccount = models.ForeignKey(User, on_delete=models.CASCADE)
    Emp_Id = models.CharField(max_length=45)
    First_Name = models.CharField(max_length=45)
    Last_Name = models.CharField(max_length=45)
    Address = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=45)
    Sallary = models.CharField(max_length=45)
    Status = models.CharField(max_length=45)
    Age = models.CharField(max_length=45)
    profile_pic = models.ImageField( null=True, blank=True, upload_to="profileimage/")
    qr_code = models.ImageField(upload_to='qr_codes',blank=True)
    def __str__(self):
      return self.First_Name + '|' + str(self.Last_Name)         
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.Emp_Id)
        canvas = Image.new('RGB',(290,290),'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-(self.Emp_Id)'+ '.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class LowOfficer(models.Model):
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    officer_id = models.CharField(max_length=45)
    def __str__(self):
      return self.officer_id + '|' + str(self.Employee)  

class Judge(models.Model):
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Judge_id = models.CharField(max_length=45)

    def __str__(self):
      return self.Judge_id  + '|' + str(self.Employee)

class Case(models.Model):
    Judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    LowOfficer = models.ForeignKey(LowOfficer, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=45)
    Last_Name = models.CharField(max_length=45)
    CaseType = models.CharField(max_length=45)
    Address = models.CharField(max_length=45)
    Case_Id = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=45)
    Status = models.CharField(max_length=45)
    Age = models.CharField(max_length=45)
    casefile = models.FileField(upload_to='casefile/')
    profile_pic = models.ImageField( null=True, blank=True, upload_to="plainttif profileimage/")
    qr_code = models.ImageField(upload_to='caseqr_codes',blank=True)
   
    def __str__(self):
      return self.First_Name + '|' + str(self.Case_Id)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.Case_Id)
        canvas = Image.new('RGB',(290,290),'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        cname = f'qr_code-(self.Case_Id)'+ '.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(cname,File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)  
            
class Shedule(models.Model):
    LowOfficer = models.ForeignKey(LowOfficer, on_delete=models.CASCADE)
    Judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    Case = models.ForeignKey(Case, on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now=True)
    Court_Room = models.IntegerField()
    body = models.TextField()

    def __str__(self):
        return self.body


class Comment(models.Model):
    Customer_Name = models.CharField(max_length=255)
    Writte_Comment = models.TextField()

    def __str__(self):
        return self.Customer_Name


class Decision(models.Model):
    Judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    Case = models.ForeignKey(Case, on_delete=models.CASCADE)
    Writte_Dession = models.TextField()
    Date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Judge                

class Summon(models.Model):
    Judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    LowOfficer = models.ForeignKey(LowOfficer, on_delete=models.CASCADE)
    Summon_body = models.TextField()
    def __str__(self):
      return self.officer_id         



class Assignjudge(models.Model):
    LowOfficer = models.ForeignKey(LowOfficer, on_delete=models.CASCADE)
    Judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    Case = models.ForeignKey(Case, on_delete=models.CASCADE)

    
