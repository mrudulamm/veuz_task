from django.contrib import messages, auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def Register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')

        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'this username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'this email already taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=cpassword)
                user.save()
            return redirect('login')
        else:
            messages.info(request,'this password not matching')
            return redirect('register')


    return render(request,'acccount/Register.html')

def loginUser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,'please provide correct details')
            return redirect('login')
    return render(request,'acccount/login.html')

def logOut(request):
    auth.logout(request)
    return redirect('login')


