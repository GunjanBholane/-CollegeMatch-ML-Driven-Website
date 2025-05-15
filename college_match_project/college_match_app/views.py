from django.shortcuts import render,redirect

from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import openai
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

# Load dataset
data = pd.read_csv(r'D:\F . P\Clg\college_match_project\college_match_project\college_match_app\collegematch.csv')

# Clean data
data.columns = data.columns.str.strip()
data['Branch'] = data['Branch'].str.strip().str.lower()
data['Category'] = data['Category'].str.strip().str.lower()
data['Marks'] = pd.to_numeric(data['Marks'], errors='coerce')

def filter_colleges(branch, category, marks):
    branch = branch.strip().lower()
    category = category.strip().lower()

    filtered = data[(data['Branch'] == branch) & 
                    (data['Category'] == category) & 
                    (data['Marks'] <= marks)]
    
    return list(filtered['Name of College'].unique())

def dream_college(request):
    colleges = None
    if request.method == 'POST':
        branch = request.POST.get('branch', '').strip()
        category = request.POST.get('category', '').strip()
        marks = request.POST.get('marks', '')

        try:
            marks = float(marks)
            colleges = filter_colleges(branch, category, marks)
        except ValueError:
            colleges = ["Invalid marks input. Please enter a valid number."]

    return render(request, 'dream_college.html', {'colleges': colleges})

def index(request):
    return render(request, 'index.html')
@login_required(login_url="login")
def about_us(request):
    return render(request, 'about_us.html')

def news(request):
    return render(request, 'news.html')

def top_colleges(request):
    return render(request, 'top_colleges.html')

def get_consultancy(request):
    return render(request, 'get_consultancy.html')

def scholarship(request):
    return render(request, 'scholarship.html')
def faq(request):
    return render(request, 'faq.html')
def dis(request):
    return render(request, 'dis.html')
def tc(request):
    return render(request, 'tc.html')
def privacy(request):
    return render(request, 'privacy.html')
def home(request):
    return render(request, 'home.html')
def contact(request):
    return render(request, 'contact.html')
def sitemap(request):
    return render(request, 'sitemap.html')
def login_page(request):
   if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')

      if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username")
            return redirect('login')
   
      user = authenticate(username=username, password=password)

      if user is None:
         messages.error(request, 'Invalid Password')
         return redirect('login')
      else:
         login(request,user)
         return redirect('about_us')

   return render(request,'login.html')
def register_page(request):
 if request.method=='POST':
   first_name=request.POST.get('first_name')
   last_name=request.POST.get('last_name')
   username=request.POST.get('username')
   password=request.POST.get('password')

   if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists!")
            return redirect('register')


   user=User.objects.create(
      first_name=first_name,
      last_name=last_name,
      username=username
   )
      #  password=password, this will not encrypt password
   user.set_password(password)
   user.save()

   messages.success(request, "Registration successful!")
   
   
   return redirect('login')  # not 'register'
 


 
 return render(request, 'register.html')

def logout_page(request):
   logout(request)
   return redirect('login')
       


@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})