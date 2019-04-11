from django.shortcuts import render
from .models import RealEstate
from empweb import urls
from mbrweb.models import MbrDetails


# Create your views here.
def index(request):
    return render(request,'choose_form.html')

def mortId(request):
    ##Token from the request could be used for Security...maybe???
     page='re_mortId.html'
     if request.method == "POST":
          mortID = request.POST.get('mortID','')
          print("This is the mortID: "+mortID)
          mbrUser = MbrDetails.objects.get(mortID=mortID)
          MbrDetails.objects.filter(mortID=mortID).update(status="Approved")
          print(mbrUser.status)
          print("This is the MBRUser: " + mbrUser.address)
          print('No User found;creating a new user')
          name= request.POST.get('name','')
          mortID=request.POST.get('mortID','')
          realEstateUser= RealEstate(
              name=name,
              mortID=mortID)
          page='reweb_confirmation.html'
          print("Saving New User into RealEstate DB")
     return render(request,page)

def re_confirmation(request):
  return render(request,'reweb_confirmation.html')

          
