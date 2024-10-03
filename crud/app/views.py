from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    data=Student.objects.all()
    next_id=[]
    n=Student.objects.count()
    for i in range(1,n+1):
        next_id.append(i)  
    combined=zip(data,next_id)
    context={"combined":combined}
    return render(request,"index.html",context)
def about(request):
    return render(request,"about.html")
def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save() 
        return redirect("/")
    return render(request,"index.html")
def updateData(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        return redirect("/")
    d=Student.objects.get(id=id)
    next_id=Student.objects.count()
    next_id+=1
    print(d)
    print(next_id)
    context={"d":d,"next_id":next_id}
    return render(request,"edit.html",context)
def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect("/")