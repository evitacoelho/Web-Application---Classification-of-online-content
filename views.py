from base64 import b64encode

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models.query_utils import Q
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

import authentication.appUtils as appUtils
from authentication.models import Classifier, Image, Locator

from .forms import ImageForm

# Create your views here.

def home(request):
    return render(request, "authentication/start.html")

def start(request):
    if request.method == "POST":
        emailAddress = request.POST['uname']
        pwd = request.POST['pass']
        myuser = authenticate(username=emailAddress, password=pwd)
        if myuser is None:
            print("Authentication failed")
            return render(request, "error.html", {'message': 'Authentication Failed'})
        else:
            login(request, myuser)
            form = ImageForm()
            return render(request, "authentication/classify.html", {'form': form})
        
    return render(request, "authentication/start.html")

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname =  request.POST['lname']
        emailAddress = request.POST['email']
        pwd = request.POST['pass']
        try:
            myuser = User.objects.create_user(username=emailAddress, email=emailAddress, password=pwd)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
        except: 
            print("Creation failed")
            return render(request, "error.html", {'message': 'Username already exists'})
        
        messages.success(request,"Your account has been successfully created")
        return redirect ("start")

    return render (request, "authentication/signup.html")

def reset(request):
    if request.method == "POST":
        emailAddress = request.POST['email']
        tokenGen = request.POST['token']
        password= request.POST['pass']

        user = User.objects.filter(email=emailAddress).first()

        if not default_token_generator.check_token(user, tokenGen) or not user:
            return render(request, "error.html", {'message': 'Password reset failed'})
        else:
            user.set_password(password)
            user.save()
            return render(request, "authentication/start.html",{'message': 'Password is reset'})
    return render(request, "error.html", {'message': 'Cannot be reset directly. Use Get help link (forgot password) to reset password'})


def forgot(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    # todo: generate token,
                    subject = appUtils.RESET_EMAIL_SUBJECT
                    email_template_name = "authentication/email.txt"
                    c = {
                            'email': user,
                            #'token': 1234
                            'token': default_token_generator.make_token(user),
                        }
                    message = render_to_string(email_template_name, c)
                    print(message)
                    try:
                        send_mail(subject=subject, message=message, from_email='admin@classifyApp.com',
                        recipient_list=[user], fail_silently=False)
                    except:
                        return render(request, "error.html", {'message': 'Failed to send email'})
                    return render(request, "authentication/reset.html", {'emailValue': user})
            else: return render(request, "error.html", {'message': 'User not found'})
        else: return render(request, "error.html", {'message': 'Password reset form is not valid'})

    return render(request, "authentication/forgot.html")

@login_required()
def location(request):
    if request.method == "POST":
        inputVal = request.POST['inputbox']
        mushy_response = "Swansea, Wales, UK"
        emailAddress = request.user
        locatorEntry = Locator(email= emailAddress, input = inputVal, locOutput = mushy_response)
        locatorEntry.save()
        return render(request, "authentication/location.html", {'output' : mushy_response , 'id' : locatorEntry.id})
    return render(request, "authentication/location.html")


@login_required()
def feedbackLoc(request):
    if request.method == "POST":
        id = request.POST['idVal']
        feedbackText = request.POST['feedback']
        try: 
            locatorEntry = Locator.objects.get(id = id)
            locatorEntry.feedback = feedbackText
            locatorEntry.save()
            return render(request, "authentication/location.html")
        except: 
             return render(request, "error.html", {"message": "Locator entry does not exist"})

def classMsg(boolResponse,inputValue):
    return 'Your post is extremist - \n' + inputValue if boolResponse else 'Your post is not extremist - \n' + inputValue

@login_required()
def classify(request):
    if request.method == "POST":
        try:
            inputVal = request.POST['inputbox']
            pallav_response = appUtils.textClassifier(inputVal)
            if pallav_response == None:
                return render(request, "error.html", {"message": "Unable to classify"})
            emailAddress = request.user
            classifierEntry = Classifier(email = emailAddress, input = inputVal, output = pallav_response)
            classifierEntry.save()
            form = ImageForm()
            return render(request, "authentication/classify.html", {'output': classMsg(pallav_response,inputVal), 'id':classifierEntry.id, 'form':form})
        except: 
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                image_field = form.cleaned_data['image']
                pallav_response = appUtils.imgClassifier(image_field.name)
                if pallav_response == None:
                    return render(request, "error.html", {"message": "Unable to classify"})
                emailAddress = request.user
                imageEntry = Image(email = emailAddress,input_image = image_field.name , output_image = pallav_response)
                imageEntry.save()
                form = ImageForm()
                return render(request, "authentication/classify.html", {'output': classMsg(pallav_response,image_field.name), 'id':imageEntry.id, 'form':form})
    else:
        form = ImageForm()
        return render(request, "authentication/classify.html", {'form': form})
    

@login_required()
def feedback(request):
    if request.method == "POST":
        id = request.POST['idVal']
        isClassCorrect = True if request.POST['isClassificationCorrect'] == "True" else False
        feedbackText = request.POST['feedback']
        form = ImageForm()
        try:
            classifierEntry = Classifier.objects.get(id = id)
            classifierEntry.classificationCorrect = isClassCorrect
            classifierEntry.feedback = feedbackText
            classifierEntry.save()
            return render(request, "authentication/classify.html", {'form': form})
        except:
            try:
                imageEntry = Image.objects.get(id = id)
                imageEntry.classificationCorrect = isClassCorrect
                imageEntry.feedback = feedbackText
                imageEntry.save()
                return render(request, "authentication/classify.html" , {'form': form})
            except:
                return render(request, "error.html", {"message": "Classification entry does not exist"})


@login_required()
def logout_view(request):
    logout(request)
    return render(request, "authentication/start.html")
