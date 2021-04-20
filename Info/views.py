from django.shortcuts import render

# Create your views here.

from django.db.models import Avg,Count,Max,Min,Sum
from django.conf import settings
from django.shortcuts import render,redirect
from.forms import StudentForm,RegistrationForm
from.models import Student_Data
from django.contrib.auth.models import User
from.forms import UserForm
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request,'info/index.html')

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            user=User.objects.create_user(username=name,email=email,password=password)
            if user:
                stu=Student_Data.objects.create(
                    address=request.POST.get('address'),
                    gender = request.POST.get('gender'),
                    country = request.POST.get('country'),
                    User=user,
                    marks_percentage=0

                )
                send_mail(
                    'Registration successful',
                    'Registration Successfull login link:http://127.0.0.1:8000/students/login/',
                    'snehakayala06@gmail.com',
                    [email],
                    fail_silently=True
                       )
            #form.save()
        return redirect('/info/index/')
    form = RegistrationForm()
    return render(request, 'info/register.html', {'form': form})


def stu_details(request):
    student_data= Student_Data.objects.all()
    return render(request, 'info/details.html', {'students': student_data})


def auth_user(request):
    if request.method=='POST':
     username=request.POST.get('username')
     email=request.POST.get('email')
     password=request.POST.get('password')
     confirmpassword=request.POST.get('password1')
     if password==confirmpassword:
         user=User.objects.create_superuser(username=username,email=email,password=password)
         user.save()
         return redirect('/info/details/')
    else:
        print('enter valid password')
    return render(request,'info/user.html')



def user_login(request):
    if request.method=='POST':
        user=authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user:
            login(request,user)
            #messages.info(request,"You are now logged in as {username}")
            return redirect('/info/details/')
    return render(request,'info/login.html',{})


def user_logout(request):
    logout(request)
    return redirect('/info/index/')


def user_edit(request,id):
    st_user=Student_Data.objects.get(id=id)
    if st_user:
        if request.method=='POST':
            st_user.name=request.POST.get('name')
            st_user.mobile = request.POST.get('mobile')
            st_user.email = request.POST.get('email')
            st_user.password = request.POST.get('password')
            st_user.address = request.POST.get('address')
            st_user.gender = request.POST.get('gender')
            st_user.country = request.POST.get('country')
            st_user.marks_percentage=request.POST.get('marks_percentage')
            st_user.save()
            return redirect('/info/details/')
        form = StudentForm(instance=st_user)
        return render(request,'info/edit.html',{'form':form,'id':id})
        #return render(request, 'details.html')
    return redirect('/info/details/')

def user_delete(request,id):
    st_user = Student_Data.objects.get(id=id)
    st_user.delete()
    return redirect('/info/details/')


def queries(request):
    obj1= Student_Data.objects.aggregate(Avg('marks_percentage'))
    obj2= Student_Data.objects.aggregate(Count('id'))
    obj3= Student_Data.objects.aggregate(Min('marks_percentage'))
    obj4= Student_Data.objects.aggregate(Max('marks_percentage'))
    obj5= Student_Data.objects.filter(marks_percentage__gte=70).count()
    obj6= Student_Data.objects.filter(marks_percentage__lte=35).count()
    info = {'Avg': obj1, 'Sum': obj2, 'Min':obj3,'Max':obj4,'pass':obj5,'fail':obj6}
    return render(request,'info/inform.html',{'info':info})




