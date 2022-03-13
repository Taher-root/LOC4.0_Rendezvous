from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"testpage.html")

def main_p(request):
   return HttpResponse('This is main page')

def after(request):
    return render(request,"afterlogin.html")  

def before(request):
    return render(request,"testpage.html")  

def dash(request):
    return render(request,"dashboard.html")

def maps(request):
    return render(request,"map.html")

def use(request):
    return render(request,"user.html")