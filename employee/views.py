from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import EmployeeDetails

def index(request):
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        ecode = request.POST.get('employeecode')
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        try:
            # Create the user
            user = User.objects.create_user(first_name=fn, last_name=ln, username=email, password=pwd)
            # Create the employee details entry
            EmployeeDetails.objects.create(user=user, empcode=ecode)  # Assuming EmployeeDetails has a user foreign key
            error = "no"
            return redirect('emp_login')
        except Exception as e:
            error = "yes"
    context = {'error': error}
    return render(request, 'registration.html', context)

def emp_login(request):
    return render(request, 'login.html')
