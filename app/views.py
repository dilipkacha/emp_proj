from django.shortcuts import render,HttpResponse,redirect
from  .models import emp
# Create your views here.
def index(request):
    user=emp.objects.all()
    contant={
        'user':user
    }
    return render(request,'index.html',contant)

def add(request):
    if request.method=='POST':
        nm=request.POST["emp_nm"]
        dep=request.POST["dept"]
        salary = int(request.POST.get('salary'))
        new_emp=emp(emp_nm=nm,dep=dep,salary=salary)
        new_emp.save()
        return redirect('index')
    elif request.method=='GET':
       return render(request,'add.html')
    else:
        return HttpResponse("add is not sucess")
def remove(request, emp_id=0):
    if emp_id:
        try:
            rem = emp.objects.get(id=emp_id)
            rem.delete()
            return HttpResponse("Remove successful")
        except emp.DoesNotExist:
            return HttpResponse("Employee not found")

    # If no emp_id provided, render the dropdown list
    remove = emp.objects.all()
    context = {
        'remove': remove
    }
    return render(request, 'remove.html', context)
