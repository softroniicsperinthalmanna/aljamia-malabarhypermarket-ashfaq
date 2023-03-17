from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import transaction
from django.core.exceptions import ValidationError
from datetime import date
import datetime
# from. models import Manager,Employee,User,Stockreport,Salesreport,Alert,todolist
from . models import *
# class UserRegistrationForm(UserCreationForm):
#     first_name = forms.CharField(max_length=101)
#     last_name = forms.CharField(max_length=101)
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name',
#                   'email', 'password1', 'password2']


class ManagerRegistrationForm(UserCreationForm):
    # first_name = forms.CharField(required= True, max_length=101)
    # last_name = forms.CharField(required= True, max_length=101)
    Name=forms.CharField(required=True,max_length=201)
    # email = forms.EmailField(required=True)
    MobileNumber=forms.IntegerField()
    Branch_name=forms.CharField(required=True,max_length=201)

    def clean_Name(self):
      Name = self.cleaned_data.get('Name')
      # if not category:
      # 	raise forms.ValidationError('This field is required')
      for instance in Manager.objects.all():
        if instance.Name== Name:
          raise forms.ValidationError(str(Name) + ' is already created')
      return Name
    
    def clean_Email_address(self):
      Email_address = self.cleaned_data.get('Email_address')
      # if not category:
      # 	raise forms.ValidationError('This field is required')
      for instance in User.objects.all():
        if instance.Email_address== Email_address:
          raise forms.ValidationError(str(Email_address) + ' is already created')
      return Email_address
    
    def clean_Branch_name(self):
      Name = self.cleaned_data.get('Name')
      Branch_name = self.cleaned_data.get('Branch_name')
      # if not category:
      # 	raise forms.ValidationError('This field is required')
      for instance in Branch_info.objects.all():
        if instance.Manager_name == Name:
         if instance.Branch_name != Branch_name:
           raise forms.ValidationError(str(Branch_name) + ' is not yours branch')
      return Branch_name
    
    
    def clean_MobileNumber(self):
      MobileNumber = self.cleaned_data.get('MobileNumber')
      # if not category:
      # 	raise forms.ValidationError('This field is required')
      for instance in Manager.objects.all():
        if instance.MobileNumber== MobileNumber:
          raise forms.ValidationError(str(MobileNumber) + ' is already created')
      if len(str(MobileNumber)) not in range(10,14):
         raise forms.ValidationError('You have not entered digits within limit')
      return MobileNumber



    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','Name', 
                   'email','MobileNumber','Branch_name','password1', 'password2']
    # def clean_category(self):
    #   Name = self.cleaned_data.get('Name')
    #   # if not category:
    #   # 	raise forms.ValidationError('This field is required')
    #   for instance in Manager.objects.all():
    #     if instance.Name== Name:
    #       raise forms.ValidationError(str(Name) + ' is already created')
    #   return Name

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_manager=True
        # user.first_name=self.cleaned_data.get('first_name')
        # user.last_name=self.cleaned_data.get('last_name')
        user.save()
        manager=Manager.objects.create(user=user)
        manager.Name=self.cleaned_data.get('Name')
        # manager.email=self.cleaned_data.get('email')
        manager.MobileNumber=self.cleaned_data.get('MobileNumber')
        manager.Branch_name=self.cleaned_data.get('Branch_name')
        manager.save()
        return user


# class EmployeeRegistrationForm(UserCreationForm):
#     Gender_choices=(
#        ("Male","Male"),
#        ("Female","Female"),
#     )

#     Shift_choices=(
#        ("Day","Day"),
#        ("Night","Night"),
#     )
#     username=forms.CharField(widget=forms.TextInput(attrs={'autofocus ': 'True'}))
#     Name = forms.CharField(required= True, max_length=101)
#     # last_name = forms.CharField(required= True, max_length=101)
#     Email = forms.EmailField(required= True,max_length=100)
#     Address = forms.CharField(required= True,max_length=500)
#     Dob=forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
#     Gender = forms.ChoiceField(widget=forms.Select,
#                       choices=Gender_choices)
#     MobileNumber = forms.IntegerField(required= True,)
#     Startdate = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
#     Branch_name = forms.CharField(required= True,max_length=100)
#     Shift = forms.ChoiceField(widget=forms.Select,
#                       choices=Shift_choices)
#     Department = forms.CharField(max_length=50)
#     # Username = forms.CharField(max_length=200)
#     # Password = forms.CharField(widget=forms.PasswordInput())
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields=['username','Name','Email','Address','Dob','Gender','MobileNumber','Startdate','Branch_name','Shift','Department']
#         # widgets={
#         #     'DOB':forms.DateInput(attrs={'type': 'date'}),
#         #     'Startdate':forms.DateInput(attrs={'type': 'date'}),
#         # }
    
#     @transaction.atomic
#     def save(self):
#         user=super().save(commit=False)
#         user.is_employee=True
#         # user.first_name=self.cleaned_data.get('first_name')
#         # user.last_name=self.cleaned_data.get('last_name')
#         user.save()
#         employee=Employee.objects.create(user=user)
#         employee.Name=self.cleaned_data.get('Name')
#         employee.Email=self.cleaned_data.get('Email')
#         employee.MobileNumber=self.cleaned_data.get('MobileNumber')
#         employee.Branch_name=self.cleaned_data.get('Branch_name')
#         employee.Address=self.cleaned_data.get('Address')
#         employee.Dob=self.cleaned_data.get('Dob')
#         employee.Gender=self.cleaned_data.get('Gender')
#         employee.Startdate=self.cleaned_data.get('Startdate')
#         employee.Shift=self.cleaned_data.get('Shift')
#         employee.Department=self.cleaned_data.get('Department')
#         employee.save()
#         return user 


class EmployeeRegistrationForm(forms.ModelForm):
    
    def clean_Name(self):
      Name = self.cleaned_data.get('Name')
      # if not category:
      # 	raise forms.ValidationError('This field is required')
      for instance in Employee.objects.all():
        if instance.Name== Name:
          raise forms.ValidationError(str(Name) + ' is already exists')
      return Name

    def clean_MobileNumber(self):
      MobileNumber = self.cleaned_data.get('MobileNumber')
      # if not category:
      # 	raise forms.ValidationError('This field is required')
      for instance in Employee.objects.all():
        if instance.MobileNumber== MobileNumber:
          raise forms.ValidationError(str(MobileNumber) + ' is already created')
      if len(str(MobileNumber)) not in range(10,14):
         raise forms.ValidationError('You have not entered digits within limit')
      return MobileNumber   
    
    def clean_Dob(self):
        Dob = self.cleaned_data.get('Dob')
        age = (date.today() - Dob).days / 365
        if age < 18:
            raise forms.ValidationError('You must be at least 18 years old')
        return Dob
    
    def clean_Branch_name(self):
       manager=Manager.objects.all()
       employee_manager=Employee.objects.all()
       Branch_name=self.cleaned_data.get('Branch_name')
      #  for instance in Manager:
      #  if manager.user.username == employee_manager.user.username:
       for instance in Manager.objects.all():
          if instance.Branch_name != Branch_name:
              raise forms.ValidationError(str(Branch_name) + ' is wrong branch ')
       return Branch_name     
    
    class Meta:
       model= Employee  
       fields=['Name','MobileNumber','Address','Dob','Gender','Startdate','Shift','Branch_name','Department']
       widgets={
          'Name':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto;'}),
          'MobileNumber':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto;  '}),
        #   'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
          'Address':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto;'}),
          'Dob':forms.DateInput(attrs={'class' : 'form-control','type': 'date','style': 'width: 200px; margin:auto;'}),
          'Gender':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto;'}),
          'Startdate':forms.DateInput(attrs={'class' : 'form-control','type': 'date','style': 'width: 200px; margin:auto;'}),
          'Shift':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto;'}),
          'Branch_name':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto;'}),
          'Department':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto;'}),

       }

class Employee_Update_Form(forms.ModelForm):
     class Meta:
       model= Employee  
       fields=['Name','MobileNumber','Address','Dob','Gender','Startdate','Shift','Branch_name','Department']
       widgets={
          'Name':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto;'}),
          'MobileNumber':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto;  '}),
        #   'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
          'Address':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto;'}),
          'Dob':forms.DateInput(attrs={'class' : 'form-control','type': 'date','style': 'width: 200px; margin:auto;'}),
          'Gender':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto;'}),
          'Startdate':forms.DateInput(attrs={'class' : 'form-control','type': 'date','style': 'width: 200px; margin:auto;'}),
          'Shift':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto;'}),
          'Branch_name':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto;'}),
          'Department':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto;'}),

       }


    # def clean_Name(self):   
    #   for instance in Employee.objects.all():
    #     Name = self.cleaned_data.get('Name')
    #     if instance.Name==Name:
    #       raise forms.ValidationError(Name + ' is already added')   
    #   return Name


class Employee_LoginForm(forms.ModelForm):
     # email = forms.EmailField(required=True)

     class Meta:
         model = Employee
         fields = ["Name","MobileNumber", "Branch_name","Department"]

class Sales_reportForm(forms.ModelForm):
    # def clean_date(self):
    #    date = self.cleaned_data['date']
    #    if Salesreport.objects.filter(date=date).exists():
    #       raise ValidationError("Date already exists")
    #    return date
    # def clean_Branch(self):
    #    Branch = self.cleaned_data['Branch']
    #    if Salesreport.objects.filter(Branch != Branch).exists():
       
    #       raise ValidationError("Please enter your own branch")
    #    return Branch
    # def clean_Branch(self):
      
    #   Branch = self.cleaned_data.get('Branch')
    #   # name=Manager.objects.filter(Name=Name)
    #   # if not category:
    #   # 	raise forms.ValidationError('This field is required')
    #   manager=Manager.objects.all()
    #   # for instance in Branch_info.objects.all():
    #   #  if instance.Manager_name == name.Name:
    #   if manager not in Branch:
    #        raise forms.ValidationError(str(Branch) + ' is not yours branch')
    #   return Branch
    def clean_Branch(self):
      Name = self.cleaned_data.get('Name')
      Branch = self.cleaned_data.get('Branch')
      # x=Manager.objects.all()
      # if not category:
      # 	raise forms.ValidationError('This field is required')
      for instance in Salesreport.objects.all() :
       if instance.Name == Name:
          if instance.Branch != Branch:
           raise forms.ValidationError(str(Branch) + ' is not yours branch')
      return Branch

    
    def clean_date(self):
      date = self.cleaned_data.get('date')
      # if not category:
      # 	raise forms.ValidationError('This field is required')
      for instance in Salesreport.objects.all():
        if instance.date== date:
          raise forms.ValidationError(str(date) + ' is already created')
      if date > datetime.date.today():
           raise forms.ValidationError("The date cannot be in the future!")
      return date

    class Meta:
       model= Salesreport
       fields=['Name','Branch','date','cash_values','card_sales','return_amount','discount','total_sales','net_sales','total_VAT']
       widgets={
          'Name':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'Branch':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'date':forms.DateInput(attrs={'class' : 'form-control','type': 'date' ,'style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'cash_values':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto; background-color:black; color:white; '}),
        #   'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
          'card_sales':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'return_amount':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'discount':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'total_sales':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'net_sales':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'total_VAT':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
       }

class Sales_report_update_Form(forms.ModelForm):
   
   class Meta:
       model= Salesreport
       fields=['date','cash_values','card_sales','return_amount','discount','total_sales','net_sales','total_VAT']
       widgets={
          # 'Name':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          # 'Branch':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'date':forms.DateInput(attrs={'class' : 'form-control','type': 'date' ,'style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'cash_values':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto; background-color:black; color:white; '}),
        #   'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
          'card_sales':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'return_amount':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'discount':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'total_sales':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'net_sales':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'total_VAT':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
       }


class Stock_reportForm(forms.ModelForm):
    
    def clean_Branch_name(self):
      Name = self.cleaned_data.get('Name')
      Branch_name = self.cleaned_data.get('Branch_name')
      # x=Manager.objects.all()
      # if not category:
      # 	raise forms.ValidationError('This field is required')
      for instance in Stockreport.objects.all() :
       if instance.Name == Name:
          if instance.Branch_name != Branch_name:
           raise forms.ValidationError(str(Branch_name) + ' is not yours branch')
      return Branch_name

    
    def clean_date(self):
      date = self.cleaned_data.get('date')
      # if not category:
      # 	raise forms.ValidationError('This field is required')
      for instance in Stockreport.objects.all():
        if instance.date== date:
          raise forms.ValidationError(str(date) + ' is already created')
      if date > datetime.date.today():
           raise forms.ValidationError("The date cannot be in the future!")
      return date
    class Meta:
       model=   Stockreport
       fields=['Name','Branch_name','date','cost_per_unit','stock_value','item_name','stock']
       widgets={
          'Name':forms.Select(attrs={'class' : 'form-control','style': 'width: 200px; margin:auto; background-color:black; color:white;'}),
          'Branch_name':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 200px; margin:auto; background-color:black; color:white;'}),
          'date':forms.DateInput(attrs={'class' : 'form-control','type': 'date' ,'style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'cost_per_unit':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto; background-color:black; color:white; '}),
        #   'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
          'stock_value':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'item_name':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 200px; margin:auto; background-color:black; color:white;'}),
          'stock':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          # 'UOM':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 200px; margin:auto; background-color:black; color:white;'}),

       }


class Stock_report_update_Form(forms.ModelForm):
   
    class Meta:
       model=   Stockreport
       fields=['Name','Branch_name','date','cost_per_unit','stock_value','item_name','stock']
       widgets={
          'Name':forms.Select(attrs={'class' : 'form-control','style': 'width: 200px; margin:auto; background-color:black; color:white;'}),
          'Branch_name':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 200px; margin:auto; background-color:black; color:white;'}),
          'date':forms.DateInput(attrs={'class' : 'form-control','type': 'date' ,'style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'cost_per_unit':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto; background-color:black; color:white; '}),
        #   'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
          'stock_value':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          'item_name':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 200px; margin:auto; background-color:black; color:white;'}),
          'stock':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:black; color:white;'}),
          # 'UOM':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 200px; margin:auto; background-color:black; color:white;'}),

       }


class Alert_Form(forms.ModelForm):
    class Meta:
        model=   Alert
        fields=['subject','alert']
        widgets={
            'subject':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
            'alert':forms.Textarea(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
        }


class To_do_Form(forms.ModelForm):
    def clean_task(self):
       task = self.cleaned_data.get('task')
       for instance in todolist.objects.all():
          if instance.task ==task:
             raise forms.ValidationError(str(task) + ' is already added')
       return task

    class Meta:
        model= todolist 
        fields=['priority','task','status']
        widgets={
            'priority':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
            'task':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
            'status':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
        }


class Task_Assign_Form(forms.ModelForm):
    def clean_deadline(self):
      deadline = self.cleaned_data.get('deadline')
      # if not category:
      # 	raise forms.ValidationError('This field is required')
      
      if deadline < datetime.date.today():
        raise forms.ValidationError("Deadline cannot be in past!")
      return deadline

    class Meta:
        model=taskassign
        fields=['task','deadline','assigned_to']
        widgets={
            'task':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
            'deadline':forms.DateInput(attrs={'class' : 'form-control','type': 'date' ,'style': 'width: 300px; margin:auto; background-color:white; '}),
            'assigned_to':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
            # 'Branch_name':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
        }

class Task_Update_Form(forms.ModelForm):
      class Meta:
        model=taskassign
        fields=['task','deadline','assigned_to']
        widgets={
            'task':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
            'deadline':forms.DateInput(attrs={'class' : 'form-control','type': 'date' ,'style': 'width: 300px; margin:auto; background-color:white; '}),
            'assigned_to':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
            # 'Branch_name':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
        }   

class Todo_Update_Form(forms.ModelForm):
   class Meta:
      model= todolist 
      fields=['priority','task','status']
      widgets={
            'priority':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
            'task':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
            'status':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
        }


class ReviewForm(forms.ModelForm):
   class Meta:
      model=Feedback
      fields=['Branch_name','Rating','review']
