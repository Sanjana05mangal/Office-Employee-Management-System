from django.shortcuts import render
from .models import Employee, Department, Role
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
def index(request):
     return render(request, 'index.html')
def all_emp(request):
    emps= Employee.objects.all()
    context= {
        'emps': emps
    }
    return render(request, 'all_emp.html', context)

def rem_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_remove= Employee.objects.get(id=emp_id)
            emp_to_remove.delete()
            return HttpResponse("employee deleted succesfully")
        except:
            return HttpResponse("please enter a valid ID")
    emps= Employee.objects.all()
    context= {
        'emps': emps
    }
    return render(request, 'rem_emp.html', context)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        role=request.POST['role']
        dept=request.POST['dept']
        emps=Employee.objects.all()
        if name:
            emps= emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name=dept)
        if role:
            emps=emps.filter(role__name=role)
        context={
            'emps':emps
        }
        return render(request, 'all_emp.html', context)
    elif request.method=='GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("Invalid Details")

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        role=int(request.POST['role'])
        dept=int(request.POST['dept'])
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        location=request.POST['location']
        new_emp= Employee(first_name=first_name, last_name=last_name, salary=salary, dept_id=dept, role_id=role, bonus=bonus, phone=phone)
        new_emp.save()
        return HttpResponse("employee added successfully")
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("exception")
