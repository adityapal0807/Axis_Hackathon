from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import IntegrityError
from django.core import serializers

from .models import User,Job_Description,Applied_resume,Application_status
# Create your views here.

def landing_page(request):
    # Authenticated users view their inbox
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))
    

@login_required
def index(request):
    jds=Job_Description.objects.all()
    return render(request,'hr/dashboard.html',{
        'jds':jds
    })

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "hr/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "hr/login.html")
    
def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "hr/register.html", {
                "message": "Passwords must match."
            })
        
        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "hr/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "hr/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("landing_page"))
"""
API ROUTES HERE
"""


def jd_description_analyser(request):
    if request.method == "GET":
        return render(request,'hr/jd.html')
    elif request.method=="POST":
        #the api has posted a job description

        """
            Analyse the form data over here and save the job description with other parameters
        """

        # and then show the response

def show_jd_function(request,jd_id):
    if request.method == "GET":
        try:
            jd = Job_Description.objects.get(id=jd_id)
        except:
            return JsonResponse()
