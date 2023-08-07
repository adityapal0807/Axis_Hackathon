from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import User
from django.db import IntegrityError

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
    return render(request,'hr/dashboard.html')

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

