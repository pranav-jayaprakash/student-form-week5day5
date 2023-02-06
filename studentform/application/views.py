from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, LoginForm
from .models import Student
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                student = Student.objects.get(email=email, password=password)
                if student:
                    return HttpResponse('USER IS VALID')
                    pass
                else:
                    return HttpResponse('INVALID USER')
                    
                    pass
            except Student.DoesNotExist:
                return HttpResponse('INVALID USER')
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
