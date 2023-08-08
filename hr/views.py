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
import json
import os
from .helpers import jd_suggestor,convert_to_text,resume_scorer,rank_resume
from .forms import *
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

        # checking from response
        print(request.POST['jobTitle'])

        """
            Analyse the form data over here and save the job description with other parameters
        """

        # and then show the response
        return render (request, 'hr/jd.html')

def analyse_resumes(request):
    if request.method=="POST":
        form = jd_submission_form(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data
            objects = []
            dropdown_item = form.cleaned_data['dropdown_field']
            job_description = dropdown_item.job_description
            pdf_files = request.FILES.getlist('pdf_files')
            print(dropdown_item.job_description)
            print(len(pdf_files))
            for pdf in pdf_files:
                file_extension = os.path.splitext(pdf.name)[-1].lower()
                content = resume_scorer(job_description,convert_to_text(pdf, file_extension))
                objects.append(content)
            print(objects)
            # ranking the documents

            ranking_data = rank_resume(job_description,objects,)
            print(ranking_data)
            
            # after this should redirect to new page with analysed resumes and their rankings
        return render(request, 'hr/analyse_resumes.html',{
            'objects':ranking_data
        })
    else:
        form= jd_submission_form()
        return render(request, 'hr/analyse_resumes.html', context={'form':form})

def show_jd_function(request,jd_id):
    if request.method == "GET":
        try:
            jd = Job_Description.objects.get(id=jd_id)
        except:
            return JsonResponse()

@csrf_exempt
def analyse_js_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        job_description = data['job_description']

        response = jd_suggestor(str(job_description))
        return JsonResponse(response,safe=False)
    

