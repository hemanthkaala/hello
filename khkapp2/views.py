from django.shortcuts import render

# Create your views here.
def jinja(request):
    return render(request,"khkapp2(1).html",context={"a":100,"b":289,"c":359})
def forr(request):
    return render(request,"khkapp2(2).html",context={"name":"hemanth"})