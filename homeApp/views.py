from django.shortcuts import render,redirect
from homeApp.models import *
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

rollno=0

# Create your views here.
def index(request):
    return render(request,'index.html')

def update_feedback(request,roll):
    f=Student_sub_fac_feedback.objects.get(pk=roll)
    return render(request,'feedback.html',{'f':f})

def logIN(request):
    print("login")
    if request.method=="POST":
        username = request.POST.get('username')
        request.session['username']=username
        print(rollno)
        password = request.POST.get('password')

        #check if user has enter correct credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            # return redirect("feedback")
            return redirect('/feedback/')
            #return render(request,"feedback.html")

        else:
            return redirect("/login")
            # Return an 'invalid login' error message.
        
    return render(request,"login.html")

def feedback(request):
    print("hii")
    if request.method=="POST":
        print(rollno)
        f_fac1_field1=request.POST.get('f_fac1_field1')
        f_fac1_field2=request.POST.get('f_fac1_field1')
        f_fac1_field3=request.POST.get('f_fac1_field1')
        f_fac1_field4=request.POST.get('f_fac1_field1')
        f_fac1_field5=request.POST.get('f_fac1_field1')
        f_fac1_field6=request.POST.get('f_fac1_field1')
        f_fac1_field7=request.POST.get('f_fac1_field1')
       # print(f_fac1_field1)
        f_fac2_field1=request.POST.get('f_fac2_field1')
        f_fac2_field2=request.POST.get('f_fac2_field1')
        f_fac2_field3=request.POST.get('f_fac2_field1')
        f_fac2_field4=request.POST.get('f_fac2_field1')
        f_fac2_field5=request.POST.get('f_fac2_field1')
        f_fac2_field6=request.POST.get('f_fac2_field1')
        f_fac2_field7=request.POST.get('f_fac2_field1')
       # print(f_fac2_field1)
        f_fac3_field1=request.POST.get('f_fac3_field1')
        f_fac3_field2=request.POST.get('f_fac3_field1')
        f_fac3_field3=request.POST.get('f_fac3_field1')
        f_fac3_field4=request.POST.get('f_fac3_field1')
        f_fac3_field5=request.POST.get('f_fac3_field1')
        f_fac3_field6=request.POST.get('f_fac3_field1')
        f_fac3_field7=request.POST.get('f_fac3_field1')
       # print(f_fac3_field1)
        f_fac4_field1=request.POST.get('f_fac4_field1')
        f_fac4_field2=request.POST.get('f_fac4_field1')
        f_fac4_field3=request.POST.get('f_fac4_field1')
        f_fac4_field4=request.POST.get('f_fac4_field1')
        f_fac4_field5=request.POST.get('f_fac4_field1')
        f_fac4_field6=request.POST.get('f_fac4_field1')
        f_fac4_field7=request.POST.get('f_fac4_field1')
       # print(f_fac4_field1)
        f_fac5_field1=request.POST.get('f_fac5_field1')
        f_fac5_field2=request.POST.get('f_fac5_field1')
        f_fac5_field3=request.POST.get('f_fac5_field1')
        f_fac5_field4=request.POST.get('f_fac5_field1')
        f_fac5_field5=request.POST.get('f_fac5_field1')
        f_fac5_field6=request.POST.get('f_fac5_field1')
        f_fac5_field7=request.POST.get('f_fac5_field1')
       # print(f_fac5_field1)
        username=request.session.get('username')
        Feedback_table=Student_sub_fac_feedback.objects.filter(roll=username).update(f_fac1_field1=f_fac1_field1,f_fac1_field2=f_fac1_field2,f_fac1_field3=f_fac1_field3,f_fac1_field4=f_fac1_field4,f_fac1_field5=f_fac1_field5,f_fac1_field6=f_fac1_field6,f_fac1_field7=f_fac1_field7, f_fac2_field1=f_fac2_field1,f_fac2_field2=f_fac2_field2,f_fac2_field3=f_fac2_field3,f_fac2_field4=f_fac2_field4,f_fac2_field5=f_fac2_field5,f_fac2_field6=f_fac2_field6,f_fac2_field7=f_fac2_field7, f_fac3_field1=f_fac3_field1 ,f_fac3_field2=f_fac3_field2 ,f_fac3_field3=f_fac3_field3 ,f_fac3_field4=f_fac3_field4 ,f_fac3_field5=f_fac3_field5 ,f_fac3_field6=f_fac3_field6 ,f_fac3_field7=f_fac3_field7  ,f_fac4_field1=f_fac4_field1,f_fac4_field2=f_fac4_field2,f_fac4_field3=f_fac4_field3,f_fac4_field4=f_fac4_field4,f_fac4_field5=f_fac4_field5,f_fac4_field6=f_fac4_field6,f_fac4_field7=f_fac4_field7, f_fac5_field1=f_fac5_field1,f_fac5_field2=f_fac5_field2,f_fac5_field3=f_fac5_field3,f_fac5_field4=f_fac5_field4,f_fac5_field5=f_fac5_field5,f_fac5_field6=f_fac5_field6,f_fac5_field7=f_fac5_field7 )
        print(Feedback_table)
        #Feedback_table.save()
        #for i in Feedback_table:
            #print('i')
            #print(i)
            #i.save()

    #list=Student_sub_fac_feedback.objects.all()
    list=Student_sub_fac_feedback.objects.filter(roll='2005001').values()
    #print(list)
    return render(request,'feedback.html',{'list':list})

'''def emoji(request):
    #searchword=request.GET.get('search')
    list=Student_sub_fac_feedback.objects.filter(roll='2005001').values()
    if request.method=="POST":
        feedback=request.POST.get('feedback')
        obj=Student_sub_fac_feedback(request.POST or None,instance='list')
        if obj.is_valid():
            obj.save()
            return redirect('emoji.html')  
    
    return render(request,'emoji.html',{'list':list})''' 



def logOUT(request):
    logout(request)
    return redirect("/")
