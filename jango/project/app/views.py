from django.shortcuts import render, HttpResponse, redirect
from .models import Student ,Login
from django.contrib import messages
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Server-side validation
        if len(name) >= 50:
            return HttpResponse('Name must be within 50 characters.')

        if len(phone) != 10:
            return HttpResponse('Enter a 10-digit phone number.')

        if not email.endswith('@gmail.com'):
            return HttpResponse('Enter a valid email address.')

        if password1 != password2:
            return HttpResponse('Passwords do not match.')

        student = Student(name=name, phone=phone, email=email, password1=password1, password2=password2)
        student.save()

        return HttpResponse('Sign up successfull.')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            messages.error(request, 'Please signup first...')
            return redirect('index')

        if student.password1 != password:
            messages.error(request, 'Password not matched')
            return redirect('index')
        applogin =  Login(email = email, password = password)
        applogin.save()

        messages.success(request, 'Login successful')
        

        return redirect('index')  # or wherever you want to redirect upon successful login
    return render(request, 'login.html')
