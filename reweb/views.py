from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'login.html')

def mortId(request):
    ##Token from the request could be used for Security...maybe???
    print(request.POST)
    return render(request,'mortId.html')