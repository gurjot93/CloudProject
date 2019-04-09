from django.shortcuts import render
from .models import MbrDetails


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
	page='register.html'
	if request.method == "POST":
		print('No User found;creating a new user')
		name= request.POST.get('name','')
		address=request.POST.get('address','')
		number=request.POST.get('number','')
		emp_details=request.POST.get('emp_details','')
		status=request.POST.get('status','')
		mbrUser= MbrDetails(
			name= name,
   			address = address,
   			number =number,
   			emp_details = emp_details,
			status=status)
		print("Saving New User into MbrDetails DB")
		mbrUser.save()
		mbrUsers =MbrDetails.objects.all()
		print(mbrUsers)
		print(request.POST)
	return render(request,page)

def confirmation(request):
	return render(request,'confirmation.html')

def formdetails(request):
	return render(request,'formdetails.html')

def login(request):
	return render(request,'login_mbr.html')