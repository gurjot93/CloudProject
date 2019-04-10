from django.shortcuts import render
from .models import MbrDetails
import random
import string


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
	page='register.html'
	return render(request,page)

def confirmation(request):
	if request.method == "POST":
		username=request.POST.get('username','')
		password= request.POST.get('password','')
		name= request.POST.get('name','')
		address=request.POST.get('address','')
		number=request.POST.get('number','')
		emp_details=request.POST.get('emp_details','')
		mortID=createMortID()
		mbrUser= MbrDetails(
			mortID=(mortID),
			username=username,
			password=password,
			name= name,
   			address = address,
   			number =number,
   			emp_details = emp_details,)
		print("Saving New User into MbrDetails DB")
		print(request.POST)
		try:
			mbrUser.save()
			mbrUsers =MbrDetails.objects.all()
			print(mbrUsers)
			mbrUser = MbrDetails.objects.get(mortID=mortID)
			print(mbrUser.mortID)
			context ={'mbrUser':mbrUser}
		except Exception:
			context ={'mbrUser':'noUser'}
			print("Unable to save the MBRUser")
		print(request.POST)
	return render(request,'mbr_confirmation.html',context)

def formdetails(request):
	return render(request,'formdetails.html',context)

def login(request):
	page='login_mbr.html'
	context={'NoUser':'NoUser'}
	if request.method == "POST":
        ##Make sure a user exist
		try:
			mbrUser =MbrDetails.objects.get(username=request.POST.get('username',''))
			##Does the password match the user's password
			if(request.POST.get('password','') ==mbrUser.password ):
				print("User found and Logging In")
				page ='formdetails.html'
				context ={'mbrUser':mbrUser}
			else:
				print("Invalid Login attemp")
		except Exception:
				print('No User found')
	return render(request,page,context)

def createMortID():
	letters = string.ascii_lowercase.join(string.ascii_uppercase)
	return ''.join(random.choice(letters) for i in range(12))
