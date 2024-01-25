from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return HttpResponse("<b>Welcome</b>")

def coursedetails(request,courseid):
    return HttpResponse(courseid)

def calculator(request):
    c=''
    try:
        if request.method =="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
        
    except:
        c="Invalid"
    print(c)
    return render(request,"calculator.html",{'c':c})


def marksheet(request):
    if request.method =="POST":
            s1=eval(request.POST.get('subject1'))
            s2=eval(request.POST.get('subject2'))
            s3=eval(request.POST.get('subject3'))
            s4=eval(request.POST.get('subject4'))
            s5=eval(request.POST.get('subject5'))
            t=s1+s2+s3+s4+s5
            p=t*100/500
            if p>=90:
                d="A+"
            elif p>80:
                d="A"
            elif p>70:
                d="B+"
            elif p>60:
                d="B"
            elif p>50:
                d="C"
            elif p>40:
                d="D"
            else:
                d="F"
            print(t)
            data={
                'total':t,
                'per':p,
                'div':d,
            }
            return render(request,"marksheet.html",data)
    return render(request,"marksheet.html")



def homepage(request):
    return render(request,"index.html")

