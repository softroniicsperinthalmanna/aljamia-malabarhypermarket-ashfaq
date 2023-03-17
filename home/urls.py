from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from home import views as home_views
# from django.urls import reverse
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth import views as auth_view

urlpatterns = [

    path('', views.index, name='index'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),

    path("logout/",auth_views.LogoutView.as_view(), name='logout' ),    

    path('employeelogin/',views.employeelogin,name='employeelogin'), 
    path('deleteemployee/<int:pk>',views.deleteemployee, name='deleteemployee'),
    path('updateemployee/<int:pk>',views.updateemployee.as_view(), name='updateemployee'),
    path('deletetask/<int:pk>',views.deletetask, name='deletetask'),
    path('updatetask/<int:pk>',views.updatetask.as_view(), name='updatetask'),
    path('deletetodo/<int:pk>',views.deletetodo, name='deletetodo'),
    path('updatetodo/<int:pk>',views.updatetodo.as_view(), name='updatetodo'),
    path('deletealert/<int:pk>',views.deletealert, name='deletealert'),
    path('updatealert/<int:pk>',views.updatealert.as_view(), name='updatealert'),




     # path( 'logout/',auth_view.LogoutView.as_view(template_name=''), name='logout'),
#     path('managersignup/', views.managersignup, name='managersignup'),
    path('adminlogin/',  auth_views.LoginView.as_view(template_name='adminlogin.html'),
         name='adminlogin'),
    path('mgremployeedetails/', views.mgremployeedetails,
         name='mgremployeedetails'),
    path('otpverification/', views.otpverification, name='otpverification'),
    path('Dashboard/', views.Dashboard, name='Dashboard'),
    path('salesreport/', views.salesreport, name='salesreport'),
    path('salesreportdibba/', views.salesreportdibba, name='salesreportdibba'),
    path('salesreportsanayya/', views.salesreportsanayya,
         name='salesreportsanayya'),
    path('stockreport/', views.stockreport, name='stockreport'),
    path('stockreportdibba/', views.stockreportdibba, name='stockreportdibba'),
    path('stockreportsanayya/', views.stockreportsanayya,
         name='stockreportsanayya'),
    path('employeedetails/', views.employeedetails, name='employeedetails'),
    path('employeesdibba/', views.employeesdibba, name='employeesdibba'),
    path('employeessanayya/', views.employeessanayya, name='employeessanayya'),
    path('addemployee/', views.addemployee, name='addemployee'),
    path('employeeprofile/', views.employeeprofile, name='employeeprofile'),
    path('customerreviews/', views.customerreviews, name='customerreviews'),

    path('customerreviewsanayya/',
         views.customerreviewsanayya, name='customerreviewsanayya'),
    path('customerreviewsmasafi/',
         views.customerreviewsdibba, name='customerreviewsdibba'),

    path('employeeprofile/', views.employeeprofile, name='employeeprofile'),



#     path('', home_views.index, name='index'),
    path('Addemployee/', views.Addemployee, name='Addemployee'),
    path('mgrlogin/', views.login, name='mgrlogin'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('alerts/', views.alerts, name='alerts'),
    path('employeedetails/', views.employeedetails, name='employeedetails'),
    path('employee/', views.employee, name='employee'),
    path('mgrallstockreports/', views.mgrallstockreports,
         name='mgrallstockreports'),
    path('mgrallsalesreports/', views.mgrallsalesreports,
         name='mgrallsalesreports'),
    path('deletesalesreport/<int:pk>',views.deletesalesreport, name='deletesalesreport'),
    path('updatesalesreport/<int:pk>',views.updatesalesreport.as_view(), name='updatesalesreport'),
    path('updatestockreport/<int:pk>',views.updatestockreport.as_view(), name='updatestockreport'), 
    path('deletestockreport/<int:pk>',views.deletestockreport, name='deletestockreport'),


    path('OTPverification/', views.OTPverification, name='OTPverification'),
    path('Sales_Report_form/', views.Sales_Report_form, name='Sales_Report_form'),
    path('stock_report_form/', views.stock_report_form, name='stock_report_form'),
    path('taskassignment/', views.taskassignment, name='taskassignment'),
    path('stock_report_form/', views.stock_report_form, name='stock_report_form'),
    path('todolist/', views.Todolist, name='todolist'),
    path('signup/', views.register, name='signup'),
    path('manager_register/', views.manager_register, name='managersignup'),
    path('employee_register/', views.employee_register, name='employeesignup'),
    path('emplopyee/', views.employee, name='employee'),
    path('Home/', views.Home, name='Home'),
    path('alertstaff/', views.alertstaff, name='alertstaff'),
    path('profile/', views.profile, name='profile'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('qrgen/', views.qrgen, name='qrgen'),


]
