from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView , CreateView
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth.models import User
from courtmanagement import models
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def managerlogin(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('/manager')

	context = {}
	return render(request, 'mang/managerlogin.html',context)

def officerlogin(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('/officer')

	context = {}
	return render(request, 'officer/officerlogin.html',context)	

def judgelogin(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('/judge')

	context = {}
	return render(request, 'judge/judgelogin.html',context)

def Welcomepage(request):
	
	return render(request, 'index.html', {})	

def shedule(request):

	form = SheduleForm()

	if request.method == 'POST':
		form = SheduleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/officer')
			
	context = {'form':SheduleForm}
	return render(request, 'officer/shedule.html', context)


def lowofficerpage(request):
	
	return render(request, 'officer/lowofficerpage.html',  {})	

def judgepage(request):  
	
	return render(request, 'judge/judgepage.html',  {})	

def home(request):
	return render(request, 'home.html',  {})	

def manager(request):
	return render(request, 'mang/manager.html',  {})		


def createaccount(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Account was created successfully for ')
			return redirect('/manager')
        
	context = {'form': CreateUserForm}

	return render(request, 'mang/createaccount.html', context)


def summon(request):
	form = SummonModel(request.POST)
	if request.method == 'POST':
		
		if form.is_valide():
		    form.save()
		    return redirect('/judge')
	
	return render(request, 'judge/summon.html', {'forms':SummonModel()})

	
def employeereg(request):

	form = EmployeeForm()

	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/manager')
			
	context = {'form':EmployeeForm}
	return render(request, 'mang/employeereg.html', context)
 
def casestore(request):

	form = CaseForm()

	if request.method == 'POST':
		form = CaseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/officer')

			
	context = {'form':CaseForm}
	return render(request, 'officer/casestore.html', context) 

def decisionpage(request):

	form = DecisionForm()

	if request.method == 'POST':
		form = DecisionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/judge')
	context = {'form':DecisionForm}
	return render(request, 'judge/decisionpage.html', context) 	

def summonpage(request):

	form = SummonForm()

	if request.method == 'POST':
		form = SummonForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/officer')
			
	context = {'form':SummonForm}
	return render(request, 'judge/summonpage.html', context)	


def commentpage(request):

	form = CommentForm()

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
			
	context = {'form':CommentForm}
	return render(request, 'commentpage.html', context)	

def assignjudgepage(request):

	form = AssignjudgeForm()

	if request.method == 'POST':
		form = AssignjudgeForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':AssignjudgeForm}
	return render(request, 'officer/assignjudgepage.html', context)		


class CommentList(ListView):
	model = Comment


def searchbar(request):
	if request.method == "POST":
		search = request.POST['search']
		employees = Employee.objects.filter(Emp_Id__contains=search)

		return render(request,'searchbar.html',{'search':search,'employees':employees})

	else:
		return render(request,'searchbar.html',{})

def show_emp(request, employee_id):
	employee = Employee.objects.get(pk=employee_id)
	return render(request, 'mang/show_emp.html', {'employee':employee})

def show_case(request, case_id):
	case = Case.objects.get(pk=case_id)
	return render(request, 'judge/show_case.html', {'case':case})	

def logout_request(request):
	logout(request)
	messages.info(request,"logged out seccessfully")
	return redirect('home')

def list_emp(request):
	employee_list = Employee.objects.all()
	return render(request,'courtmanagement/employee_list.html',{'employee_list':employee_list})

def list_account(request):
	user_list = User.objects.all()
	return render(request,'courtmanagement/account_list.html',{'user_list':user_list})

def list_case(request):
	case_list = Case.objects.all()
	return render(request,'courtmanagement/case_list.html',{'case_list':case_list})	


def list_judgecase(request):
	case_list = Case.objects.all()
	return render(request,'courtmanagement/judgecase_list.html',{'case_list':case_list})	

def list_assignedcase(request):
	case_list = Case.objects.all()
	assignjudge_list = Assignjudge.objects.all()
	return render(request,'courtmanagement/assignjudge_list.html',{'assignjudge_list':assignjudge_list, 'case_list':case_list})		

def list_shedule(request):
	shedule_list = Shedule.objects.all()
	return render(request,'courtmanagement/shedule_list.html',{'shedule_list':shedule_list})			

def update_case(request, case_id):
	case = Case.objects.get(pk=case_id)

	form = CaseForm(request.POST or None, instance=case)
	if form.is_valid():
		form.save()
		return redirect('/officer')
	return render(request, 'officer/update_case.html', {'case':case,'form':form})	

def update_empreg(request, employee_id):
	employee = Employee.objects.get(pk=employee_id)

	form = EmployeeForm(request.POST or None, instance=employee)
	if form.is_valid():
		form.save()
		return redirect('/manager')
	return render(request, 'mang/update_empreg.html', {'employee':employee,'form':form})	

def update_account(request, user_id):
	user = User.objects.get(pk=user_id)

	form = UserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('/manager')
	return render(request, 'mang/update_account.html', {'user':user,'form':form})	

	