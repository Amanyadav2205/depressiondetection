import json
from multiprocessing import context
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth import authenticate , login , logout
from django.urls import reverse
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from home.models import Contact
from django.contrib import messages
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    context = {
        'variable': "this is sent"
    }

# def signup(request):
#     #Information you want from user
#     if request.method == "POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         number = request.POST['number']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

#         # Check if the username already exists
#         if not User.objects.filter(username='your_desired_username').exists():
#     # Username is unique; you can create the user
#          user = User.objects.create_user('your_desired_username', 'your_email@example.com', 'your_password')
#         else:
#         # Handle the case where the username already exists
#          print("Username already exists")


#         #Information you want to save in database
#         myuser = User.objects.create_user(name,email,pass1)
#         myuser.number = number
#         myuser.save()

#         messages.success(request,"Your Account has been created")

#         #Redirect user to loginpage
#         return redirect('signin.html')
    
#     # return HttpResponse("this is homepage")
#     return render(request, 'signup.html')


def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check if the username already exists
        if not User.objects.filter(username=name).exists():
            # Username is unique; you can create the user
            user = User.objects.create_user(name, email, pass1)
            user.number = number
            user.save()

            messages.success(request, "Your Account has been created")

            # Redirect user to the 'signin' page
            return redirect('signin')

        else:
            # Handle the case where the username already exists
            print("Username already exists")

    return render(request, 'signup.html')


def signin(request):
 if request.method == 'POST':
        name = request.POST['name']     
        pass1 = request.POST['pass1']     

        user = authenticate(name = name, password= pass1)

        if user is not None:
            login(request, user)
            name = user.name
            return render(request , "home/index.html")
        
        else:
            messages.error(request , "bad Credentials")
            return redirect('home')    



 return render(request ,"signin.html")





def signout(request):
    return render(request, "home/signout.html")


def about(request):

    # return HttpResponse("this is about page")
    return render(request, 'about.html')

def base(request):
    return render(request, 'base.html')

def services(request):
    # return HttpResponse("this is services page")
    return render(request, 'services.html')
def contact(request):
    # return HttpResponse("this is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        textarea = request.POST.get('textarea')
        contact = Contact(name=name,email=email,phone=phone,textarea = textarea,date = datetime.today())
        contact.save()

        messages.success(request, "Your message has been sent.")

    return render(request, 'contact.html')


def face_view(request):
    return render(request, 'face.html')
    
from django.shortcuts import render





def index(request):
    return render(request, 'index.html')
def course(request):
    # Your view logic here
    return render(request, 'course.html')
def pricing(request):
    return render(request,'pricing.html')
def asement_view(request):
   
    # Specify the path to your JSON file
    json_file_path = 'questions.json'  # Update with the correct file path

    try:
        with open(json_file_path) as json_file:
            questions = json.load(json_file)
    except FileNotFoundError:
        # Handle the case where the JSON file is not found
        # You can display an error message or perform other actions here
        questions = []

    context = {
        'questions': questions,
    }

    return render(request, 'Asement.html', context)

def result_view(request):
    return render(request, 'result.html')
    