from django.shortcuts import render
from .models import MbrDetails


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
		mbrUser= MbrDetails(
			username=username,
			password=password,
			name= name,
   			address = address,
   			number =number,
   			emp_details = emp_details,)
		print("Saving New User into MbrDetails DB")
		print(request.POST)
		mbrUser.save()
		##mbrUsers =MbrDetails.objects.all()
		##print(mbrUsers)
		##print(request.POST)
	##mbrUser = MbrDetails.objects.get(username=username)
	##print(mbrUser.mortID)
	##context ={'mbrUser':mbrUser}
	return render(request,'mbr_confirmation.html')

def formdetails(request):
	try:
		mbrUsers =MbrDetails.objects.all()
		##print("This is the name: " +mbrUsers[1].name)
		print(mbrUsers)
		##mbrUser = MbrDetails.objects.get(address='test')
		##context ={'mbrUser':mbrUser}
	except Exception:
		print("Error getting MBRUsers")
	return render(request,'formdetails.html')
	##return render(request,'formdetails.html',context)

def login(request):
	page='login_mbr.html'

	if request.method == "POST":
        ##Make sure a user exist
		try:
			employee =MbrDetails.objects.get(username=request.POST.get('username',''))
			print(employee.password)
			##Does the password match the user's password
			if(request.POST.get('password','') ==employee.password ):
				page ='formdetails.html'
			else:
				print("Invalid Login attemp")
		except Exception:
				print('No User found')

	return render(request,page)