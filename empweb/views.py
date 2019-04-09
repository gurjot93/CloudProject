from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    page='login.html'

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
    employees =Employee.objects.all()
    ##username = "this"
    ##password = "password"
    ##Make sure a user exist
    try:
        employee =Employee.objects.get(username=username)
        ##Does the password match the user's password
        if(password ==employee.password ):
            page ='mortId.html'
        else:
             print("Invalid Login attemp")
    except Exception:
        print('No User found')

    ##print(employee.password)
    print(employees)
    return render(request,page)

def mortId(request):
    ##Token from the request could be used for Security...maybe???
    print(request.POST)
    
    

    ##Add a User
    ##username = request.POST["username"]
    ##password = request.POST["password"]
    ##employee= Employee(username=username,password=password)
    ##employee.save()
    ##print("The Username is "+username)
    ##print("The passowrd is "+password)
    return render(request,'mortId.html')

def create_user(request):
##Add a User
    return render(request,'create_user.html')