from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    page='login.html'
    employees =Employee.objects.all()
    print(employees)
    if request.method == "POST":
        ##Make sure a user exist
        try:
            employee =Employee.objects.get(username=request.POST.get('username',''))
            print(employee.password)
            ##Does the password match the user's password
            if(request.POST.get('password','') ==employee.password ):
                page ='mortId.html'
            else:
                print("Invalid Login attemp")
        except Exception:
            print('No User found')
    return render(request,page)

def mortId(request):
    ##Token from the request could be used for Security...maybe???
    print(request.POST)
    return render(request,'mortId.html')

def create_user(request):
##Add a User
    page='login.html'
    if request.method == "POST":
        employee_name= request.POST.get('name','')
        startDate=request.POST.get('startDate','08/04/2019')
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        salary = request.POST.get('salary','0')
        employee= Employee(
            employee_name=employee_name,
            username=username,
            password=password,
            salary=salary,
            startDate=startDate)
        employee.save()
        employees =Employee.objects.all()
        print(employees)
    else:
        page='emp_create_user.html'
    return render(request,page)

def confirmation(request):
    return render(request,'confirmation.html')