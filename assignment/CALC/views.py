from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Function for checking the type of button
def Button(request):
  list_button=['btn1','btn2','btn3','btn4','btn5','btn6','btn7','btn8','btn9','btn0','btn%','btn-','btn*','btn+','btn/','btn.','btn(','btn)','btnc','btne',]
  for b in list_button:
    if b in request.POST:
      return b[3]
  return[-1]
#function for calculating the result of expression
def view_calc(request):
  if request.method=='GET':
    resp=render(request,'./CALC/calculator.html')
    return resp
  elif request.method=='POST':
    d1={}
    button=Button(request)
    if(button!='c' and button!='e' and button!='%'):
        output=request.POST.get('res','NA')
        output+= button
        d1={'res':output}
        resp=render(request,'./CALC/calculator.html', context=d1)
        return resp
    elif(button=='c'):
      res=""
      d1={'res':res}
      resp=render(request,'./CALC/calculator.html', context=d1)
      return resp
    elif(button=='e'):
      res=eval(request.POST.get('res','NA'))
      d1={'res':res}
      resp=render(request,'./CALC/calculator.html', context=d1)
      return resp
    elif(button=='%'):
      res=request.POST.get('res','NA')
      res+='/100*'
      d1={'res':res}
      resp=render(request,'./CALC/calculator.html', context=d1)
      return resp
    

    

      
