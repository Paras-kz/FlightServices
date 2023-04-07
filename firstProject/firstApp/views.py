from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
# Create your views here.
def employeeview(request):
    # emp={
    #     'id':123,
    #     'name':'dharm',
    #     'sal':2000000
    # }       

    data=Employee.objects.all()
    context={'employee':list(data.values('name','sal'))}
    
    #created a dict context with key='employee' and 
    #it's value =list of above data variable which holds all Emoloyee objects

    return JsonResponse(context)                                                                                                