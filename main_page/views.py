from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"testpage.html")

def main_p(request):
   return HttpResponse('This is main page')