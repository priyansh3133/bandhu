from django.shortcuts import render
from accounts.models import User
from social_django.models import UserSocialAuth
# Create your views here.

def index(request):
    obj = UserSocialAuth.objects.all()
    obj1 = User.objects.all()
    print(obj,obj1)
    return render(request, 'landing_page.html')

def cause1(request):
    return render(request, 'cause1.html')
    
def cause2(request):
    return render(request, 'cause2.html')

def cause3(request):
    return render(request, 'cause3.html')
    
def cause4(request):
    return render(request, 'cause4.html')

def cause5(request):
    return render(request, 'cause5.html')