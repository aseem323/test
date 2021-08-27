from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testfun(request):
    return HttpResponse('function is working')
def fn2(request):
    return render(request,'sample.html')    

