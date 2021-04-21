from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestFun1(request):
    return HttpResponse('hlooooo')
def TestFun2(request):
    return HttpResponse('<h1>hloooo</h1>+')
def TestFun3(request):
    return render(request,'index.html')