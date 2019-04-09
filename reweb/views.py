from django.shortcuts import render
from .models import RealEstate
from empweb import urls


# Create your views here.
def index(request):
    return render(request,'choose_form.html')

def mortId(request):
    ##Token from the request could be used for Security...maybe???
     page='re_mortId.html'
     if request.method == "POST":
          print(request.POST)
          try:
            reaEstateUser =RealEstate.objects.get(mortID=request.POST.get('mortID',''))
            print(reaEstateUser.name)
            page='login.html'
           ##If there is no current user by that mortId then add a new user
          except Exception:
            print('No User found;creating a new user')
            name= request.POST.get('name','')
            mortID=request.POST.get('mortID','')
            realEstateUser= RealEstate(
                name=name,
                mortID=mortID)
            print("Saving New User into RealEstate DB")
            realEstateUser.save()
            realEstateUsers =RealEstate.objects.all()
            print(request.POST)
            print(realEstateUsers)
     return render(request,page)