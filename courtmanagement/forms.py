from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from django.contrib.auth.forms import UserCreationForm


class SheduleForm(ModelForm):
	class Meta:
		model = Shedule
		fields = ('LowOfficer','Judge','Case','Court_Room','body')
	
		widgets = {
		    'LowOfficer':forms.Select(attrs={'class':'form-control'}),
		    'Judge':forms.Select(attrs={'class':'form-control'}),
		    'Case':forms.Select(attrs={'class':'form-control'}),
		    'Court_Room':forms.TextInput(attrs={'class':'form-control'}),
		    'body':forms.Textarea(attrs={'class':'form-control'}),
		}

class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = ('Judge','LowOfficer', 'First_Name', 'Last_Name', 'CaseType', 'Case_Id', 'Address', 'phone_no', 'Status', 'Age','casefile', 'profile_pic','qr_code' )
        widgets = {
		    'Judge':forms.Select(attrs={'class':'form-control'}),
		    'LowOfficer':forms.Select(attrs={'class':'form-control'}),
		    'First_Name':forms.TextInput(attrs={'class':'form-control'}),
		    'Last_Name':forms.TextInput(attrs={'class':'form-control'}),
		    'CaseType':forms.TextInput(attrs={'class':'form-control'}),
		    'Case_Id':forms.TextInput(attrs={'class':'form-control'}),
		    'Address':forms.TextInput(attrs={'class':'form-control'}),
		    'phone_no':forms.TextInput(attrs={'class':'form-control'}),
		    'Status':forms.TextInput(attrs={'class':'form-control'}),
		    'Age':forms.TextInput(attrs={'class':'form-control'}),
		    #'profile_pic':forms.Button(attrs={'class':'form-control'}),
		}

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee

		fields = ('UserAccount','Emp_Id', 'First_Name', 'Last_Name', 'Address', 'phone_no', 'Sallary', 'Age','profile_pic', 'qr_code' )


		widgets = {
		    'UserAccount':forms.Select(attrs={'class':'form-control'}),
		    'Emp_Id':forms.TextInput(attrs={'class':'form-control'}),
		    'First_Name':forms.TextInput(attrs={'class':'form-control'}),
		    'Last_Name':forms.TextInput(attrs={'class':'form-control'}),
		    'Address':forms.TextInput(attrs={'class':'form-control'}),
		    'phone_no':forms.TextInput(attrs={'class':'form-control'}),
		    'Sallary':forms.TextInput(attrs={'class':'form-control'}),
		    'Status':forms.TextInput(attrs={'class':'form-control'}),
		    'Age':forms.TextInput(attrs={'class':'form-control'}),
		    #'qr_code':forms.Button(attrs={'class':'form-control'}),
		}


class DecisionForm(ModelForm):
	class Meta:
		model = Decision
		fields = ('Judge','Case','Writte_Dession') 

		widgets = {
		    'Judge':forms.Select(attrs={'class':'form-control'}),
		    'Case':forms.Select(attrs={'class':'form-control'}),
		    'Writte_Dession':forms.Textarea(attrs={'class':'form-control'}),
		}

class SummonForm(ModelForm):
	class Meta:
		model = Summon
		fields = ('Judge','LowOfficer','Summon_body')
		
		widgets = {
		    'Judge':forms.Select(attrs={'class':'form-control'}),
		    'LowOfficer':forms.Select(attrs={'class':'form-control'}),
		    'Summon_body':forms.Textarea(attrs={'class':'form-control'}),
		}	

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('Customer_Name', 'Writte_Comment')

		widgets = {
		    'Customer_Name':forms.TextInput(attrs={'class':'form-control'}),
		    'Writte_Comment':forms.Textarea(attrs={'class':'form-control'}),
		}



class AssignjudgeForm(ModelForm):
	class Meta:
		model = Assignjudge
		fields = ('LowOfficer','Judge','Case')

		widgets = {
		    'LowOfficer':forms.Select(attrs={'class':'form-control'}),
		    'Judge':forms.Select(attrs={'class':'form-control'}),
		    'Case':forms.Select(attrs={'class':'form-control'}),
		}
		

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

		widgets = {
		    'username':forms.TextInput(attrs={'class':'form-control'}),
		    'email':forms.TextInput(attrs={'class':'form-control'}),
		    'password1':forms.TextInput(attrs={'class':'form-control'}),
		    'password2':forms.TextInput(attrs={'class':'form-control'}),
		}