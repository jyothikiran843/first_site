import re
from webbrowser import get
from django.shortcuts import render,get_object_or_404
from myapp.forms import Student_Create
from myapp.models import Student
# Create your views here.

def index(request):
    all=Student.objects.all()
    return render(request,'myapp/index.html',{'students':all})

def create(request):
    form=Student_Create()
    if request.method=='POST':
        form=Student_Create(request.POST)
        if form.is_valid():
            print(request.POST)
            Student.objects.create(sname=request.POST.get('sname'),email=request.POST.get('email'),gpa=request.POST.get('gpa'),human=True if request.POST.get('human')=='on' else False)
            Student.save
            form=Student_Create()
        else:
            print("Not Valid")
            form=Student_Create()
    return render(request,'myapp/create.html',{'form':form})

def detail(request,slug=None):
    all=get_object_or_404(Student,slug=slug)
    return render(request,'myapp/detail.html',{'students':all})

def result(request):
    if request.method=="POST":  
        if request.POST.get('q')!="":
            all=Student.objects.filter(sname__contains=request.POST.get('q'))
        else:
            all=Student.objects.all()
    else:
        all=Student.objects.all()
    print(all)
    return render(request,'myapp/results.html',{'students':all})
    