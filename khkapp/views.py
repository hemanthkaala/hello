from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> hello hemanth </h1>")

# Create your views here.
def persion(request):
    d={"name":"hemanth","age":23,"add":"bangalore"}
    return render(request,"html2.html",d)

def image(request):
    return render(request,"html1.html",)

def sub(request):
    a=int(input("enter a value: "))
    b=int(input("enter b value: "))
    c=a-b
    return render(request,"html3.html",context={'a':a,'b':b,"c":c})
def add(request):
    a=int(input("enter a value: "))
    b=int(input("enter b value: "))
    c=a+b
    return render(request,"html4.html",context={"a":a,"b":b,"c":c})

def cal(request):
    choice=input("enter your choice: ")
    a=int(input("enter a value: "))
    b=int(input("enter b value: "))
    def add(request):
        c=a+b
        return c  
    def sub(request):
        c=a-b
        return c
    def divi(request):
        c=a%b
        return c 
    def mult(request):
        c=a*b
        return c 
    ad=add(request)
    s=sub(request)
    m=mult(request)
    d=add(request)
    return render(request,"html5.html",context={"choice":choice,"ad":ad,"m":m,"s":s,"d":d,"a":a,"b":b})