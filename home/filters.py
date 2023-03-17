import django_filters

from django_filters import DateFilter, CharFilter
from . models import *

class Salesreport_Filter(django_filters.FilterSet):
    # start_date=DateFilter(field_name="date", lookup_expr='icontains')
    # end_date=DateFilter(field_name="date", lookup_expr='icontains')
    # Day_Month_year=DateFilter(field_name="date", lookup_expr='icontains')
    class Meta:
        model = Salesreport         
        fields =  ['date']
#         # exclude=['Branch','return_amount','total_VAT','discount','user','cash_values']
class Stockreport_Filter(django_filters.FilterSet):
    item_name= CharFilter(field_name="item_name", lookup_expr='icontains')
    class Meta:
        model = Stockreport         
        fields =  ['date','item_name']

class Taskassign_Filter(django_filters.FilterSet):
      task= CharFilter(field_name="task", lookup_expr='icontains')
      deadline= DateFilter(field_name="deadline", lookup_expr='icontains') 
    #   assigned_to= CharFilter(field_name="assigned_to", lookup_expr='assigned_to__icontains') 
      class Meta:
        model = taskassign         
        fields =  ['task','deadline','assigned_to']

class Employee_Filter(django_filters.FilterSet):
    Name=CharFilter(field_name="Name",lookup_expr='icontains')
    Department=CharFilter(field_name="Department",lookup_expr='icontains')

    class Meta:
        model=Employee
        fields=['Name','Department']

class Todo_Filter(django_filters.FilterSet):
    # priority=CharFilter(field_name="priority")
    task=CharFilter(field_name="task",lookup_expr='icontains')
    # status=CharFilter(field_name="task")

    class Meta:
        model=todolist
        fields=['priority','task','status']        

class Alert_Filter(django_filters.FilterSet):

    subject=CharFilter(field_name="subject",lookup_expr='icontains')  

    class Meta:
        model=todolist
        fields=['subject']    

# class Stockreport_Filter(django_filters.FilterSet):
#     start_date=DateFilter(field_name="date", lookup_expr='gte')
#     end_date=DateFilter(field_name="date", lookup_expr='lte')
#     class Meta:
#         model = Stockreport
#         fields =  ['date']        