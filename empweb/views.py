from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    page='login.html'
    employees =Employee.objects.all()
    username = request.POST.get("username",'')
    password = request.POST.get("password",'')
    ##Make sure a user exist
    try:
        employee =Employee.objects.get(username=request.POST["username"])
        ##Does the password match the user's password
        if(password ==employee.password ):
            page ='mortId.html'
        else:
             print("Invalid Login attemp")
    except Exception:
        print('No User found')

    ##print(employee.password)
    ##print(employees)
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