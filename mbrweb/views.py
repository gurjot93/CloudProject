from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
	return render(request,'register.html')

def confirmation(request):
	return render(request,'confirmation.html')

def formdetails(request):
	return render(request,'formdetails.html')

def login(request):
	return render(request,'login_mbr.html')