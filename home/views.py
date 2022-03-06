from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from home.models import Task
# Create your views here.

def home(request):
    return render(request,'home.html')

def booking(request):
    if request.user.is_authenticated:
        context={'success': False}
        if request.method == "POST":
            user = request.user
            fullname = request.POST['fullname']
            email = request.POST['email']
            room = int(request.POST['room'])
            member = int(request.POST['member'])
            date = request.POST['date']
            days = int(request.POST['days'])
            
            #save the data in database
            d=Task(
                user=user,
                fullname=fullname,
                email=email,
                room=room,
                no_of_members=member,
                no_of_days=days,
                start_date=date
                
            )
            d.save()
            context={'success':True}
        return render(request,'booking.html',context)
    else:
        return redirect('login')
def status(request):
    if request.user.is_authenticated:
        alldata = Task.objects.filter(user=request.user)
        context={'tasks':alldata}
        return render(request,'status.html',context)
        
    else:
        return redirect('login')
def login_user(request):
    #if get request normal render the page
    if request.method == "POST":
        username = request.POST["user"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,"home.html")
        else:
            return render(request,'login.html',{'message':'Login failed'})
    
    return render(request,"login.html",{'message':''})    

def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    
    return render(request, "register.html", context)
def logout_user(request):
    logout(request)
    return redirect("home")
