from django.shortcuts import render,redirect
from SMS.models import *
from django.http import HttpResponse

# Create your views here.
def Home(request):
    if request.method=='GET':
      resp=render(request,'SMS/home.html')
      return resp
    elif request.method=='POST':
       if 'btnadd' in request.POST:
        stu=Student()
        stu.name=request.POST.get('name','NA')
        stu.age=int(request.POST.get('age',0))
        stu.mobileno=request.POST.get('mobileno','NA')
        stu.address=request.POST.get('address','NA')
        stu.save()
        stu=Student.objects.all()
        d1={'stu':stu}
        resp=render(request,'SMS/page2.html',context=d1)
        return resp
def page2(request):
    if request.method=='GET':
      stu=Student.objects.all()
      d1={'stu':stu}
      resp=render(request,'SMS/page2.html',context=d1)
      return resp
           
def delete(request,id):
   Student.objects.filter(id=id).delete()
   return redirect('/sms/home/page2.html')
def edit(request, id):
   if request.method=='GET':
     student=Student.objects.filter(id=id)
     resp=render(request,'SMS/edit.html',context={'student':student})
     return resp
   
   elif request.method=='POST':
   

        s=Student()
        if Student.objects.filter(id=id).exists():
         s.name=request.POST.get('name','NA')
         s.age=int(request.POST.get('age',0))
         s.mobileno=request.POST.get('mobileno','NA')
         s.address=request.POST.get('address','NA')
         Student.objects.filter(id=id).update(name=s.name,age=s.age,mobileno=s.mobileno,address=s.address)
         return redirect('/sms/home/page2.html')
         
            
            
      
