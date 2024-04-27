from django.core.checks import messages

from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login, logout,authenticate
from .forms import CustomerVerificationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User




def survey_types(request):
    # Your logic to get survey types and counts goes here
    survey_types_data = [
        ('Customers', 45),
        ('Education', 24),
        ('Employees', 76),
        ('Events', 11),
        ('Forms', 68),
        ('Healthcare', 24),
        ('Market Research', 60),
        ('Nonprofit', 5),
        ('Other', 51),
    ]

    return render(request, 'recentsurveys.html', {'survey_types_data': survey_types_data})


def customersurvey(request):
    if request.method == 'POST':
        form = CustomerVerificationForm(request.POST)
        if form.is_valid():
            return HttpResponse("Verification Successful!")
    else:
        form = CustomerVerificationForm()

    return render(request, 'customersurvey.html', {'form': form})

from .forms import FeedbackForm


def websitefeedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')  # Thank you page template
    else:
        form = FeedbackForm()
    return render(request, 'websitefeedback.html', {'form': form})

def secondnavbar(request):
    return render(request, 'secondnavbar.html')

def customers(request):
    return render(request, 'customers.html')

def form1(request):
    return render(request, 'form1.html')


from django.shortcuts import render
from django.http import HttpResponse


def form2(request):
    if request.method == 'POST':
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        response = f"Address Verification Result: {street}, {city}, {state} {zipcode}"
        return HttpResponse(response)
    else:
        return render(request, 'form2.html')


def navbar(request):
    return render(request, 'navbar.html')

def fhome(request):
    return render(request, 'firsthomepage.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        entered_captcha = request.POST.get('entered_captcha')
        generated_captcha = request.session.get('captcha')

        if len(username) >= 6 and len(password) >= 6 and entered_captcha == generated_captcha:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'login.html')  # Adjust 'home' to the name of your home page URL
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Login failed. Please check your credentials and CAPTCHA.')
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def home(request):
    return render(request, 'home.html')

def survey_create(request):
    if request.method == 'POST':
        survey_title = request.POST.get('surveyTitle')
        questions = request.POST.getlist('question[]')
        return render(request, 'survey.html', {'survey_title': survey_title})

    return render(request, 'survey.html')



def signup(request):
    return render(request, 'signup.html')

import re
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def signup1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if len(username) != 8:
            messages.error(request, 'Username must be exactly 8 characters long')
            return redirect('signup')

        if not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            messages.error(request, 'Password must contain at least one alphabet, one number, one special character, and be 8 characters long')
            return redirect('signup')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('home')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


from django.shortcuts import render
from django.http import HttpResponse


def edform1(request):
    return render(request, 'edform1.html')

def educational(request):
    return render(request, 'educational.html')


