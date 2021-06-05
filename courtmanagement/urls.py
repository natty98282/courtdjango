
from django.urls import path, include
from . import views 
from django.contrib import admin
from courtmanagement.views import *

urlpatterns = [
    path('judge/', views.judgepage, name='judgepage'),
    path('officer/', views.lowofficerpage, name='lowofficerpage'),
    path('home/', views.home, name='home'),
    path('', views.Welcomepage, name='Welcomepage'),
    path('manager/', views.manager, name='manager'),
    path('assign/', views.assignjudgepage, name='assignjudgepage'),
    path('shedule/', views.shedule, name='shedule'),
    path('commentpage/', views.commentpage, name='commentpage'),
    path('createaccount/', views.createaccount, name='createaccount'),
    path('summonpage/', views.summonpage, name='summonpage'),
    path('employeereg/', views.employeereg, name='employeereg'),
    path('casestore/', views.casestore, name='casestore'),
    path('decisionpage/', views.decisionpage, name='decisionpage'),
    path('comment_list/', views.CommentList.as_view()),
    path('case_list/', views.list_case,name='case-list'),
    path('jcase_list/', views.list_judgecase,name='judgecase-list'),
    path('account_list/', views.list_account,name='account-list'), 
    path('shedule_list/', views.list_shedule,name='shedule-list'),
    path('assignjudge_list/', views.list_assignedcase,name='assignjudge-list'),
    path('employee_list/', views.list_emp, name='employee_list'),
    path('searchbar/',views.searchbar,name='searchbar'),
    path('show_emp/<employee_id>',views.show_emp,name='show-emp'),
    path('show_case/<case_id>',views.show_case,name='show-case'),
    path('update_case/<case_id>',views.update_case,name='update-case'),
    path('update_account/<user_id>',views.update_account,name='update-account'),
    path('update_empreg/<employee_id>',views.update_empreg,name='update-empreg'),
    path('managerlogin/', views.managerlogin, name='managerlogin'),
    path('officerlogin/', views.officerlogin, name='officerlogin'),
    path('judgelogin/', views.judgelogin, name='judgelogin'),
    path('logout/',views.logout_request,name='logout'),


]

