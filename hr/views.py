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
from .helpers import jd_suggestor,convert_to_text,resume_scorer,rank_resume,candidate_login_credential,generate_questions
from .forms import *
from .models import User,Job_Description,Applied_resume
import uuid
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
    jds=Job_Description.objects.filter(hr_id = request.user).all()
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
        return render(request, 'hr/jd.html')
    elif request.method=="POST":
        #the api has posted a job description

        job_title = request.POST['jobTitle']
        skills = request.POST['skills']
        responsibilities = request.POST['responsibilities']
        requirements = request.POST['requirements']
        about_company = request.POST['aboutCompany']

        # Create and save the job description instance
        job_description = {
            'job_title': job_title,
            'skills': skills,
            'responsibilities': responsibilities,
            'requirements': requirements,
            'about_company': about_company
        }

        hr_id = request.user  # Assuming the user is logged in as an HR user
        jd_instance = Job_Description(hr_id=hr_id, jd_title=job_title, job_description=job_description)
        jd_instance.save()

        # Show the response
        return HttpResponseRedirect(reverse('index'))

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
            request.session['ranking_data']= ranking_data
            print(ranking_data)

            #temporarily saving applied resume
            
            # send mail for candidates
            for rank in ranking_data:

                obj1 = Applied_resume(
                    jd_id = dropdown_item,
                    applicant_email=rank['Person_Email_ID'],
                    resume_score=rank['Score'],
                    resume_rank=rank['Rank'],
                    resume_level=rank['level'],
                    resume_summary=rank['Short_Summary'],
                    resume_rank_reason=rank['Reason'],
                    resume_selected=False
                )
                obj1.save()

                
                # email = rank['Person_Email_ID']
                # password =str(uuid.uuid4().int)[:10]

                # # create an candidate account with this user
                # user = User.objects.create_user(email, email, password)
                # user.is_hr = False
                # user.save()

                

                # #send Email
                # candidate_login_credential(email,password)


                # obj = TEST_CREDENTIALS(candidate_id = user,resume_id = obj1)
                # obj.save()
            
            # after this should redirect to new page with analysed resumes and their rankings
        return HttpResponseRedirect(reverse(ranked_resumes))
        # return render(request, 'hr/analyse_resumes.html',{
        #     'objects':ranking_data,
        # })
    else:
        form= jd_submission_form()
        return render(request, 'hr/analyse_resumes.html', context={'form':form})

def ranked_resumes(request):
    if request.method=="POST":
        try:
            data = json.loads(request.body)
            selected_emails = data.get('selected_emails', [])

            # Process the selected email IDs here
            # ...

            print(selected_emails)
        except:
            print("data not recieved")
            
        return HttpResponseRedirect(reverse(jd_description_analyser))
    else:
        ranking_data=request.session.get('ranking_data')
        ranking_data_json= json.dumps(ranking_data)
        return render(request, "hr/resume_ranking.html", context={'ranking_data':ranking_data_json})
    
def JD_Progress(request,jd_id):
    # load the jd
    jd = Job_Description.objects.get(id=jd_id,hr_id=request.user)
    applied_resumes = Applied_resume.objects.filter(jd_id=jd).all()

    test_update = []
    for resume in applied_resumes:
        obj = TEST_CREDENTIALS.objects.get(resume_id=resume)
        test_update += [obj]


    return render(request,'hr/jd_progress.html',{
        'jd':jd,
        'applied_resumes' : applied_resumes,
        'test_updates':test_update
    })

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
    




"""
    Candidate Side
"""
def candidate_login(request):
    if request.method == "POST":
        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            if user.is_hr == False:
                login(request, user)
                return HttpResponseRedirect(reverse("candidate_test_window"))
            else:
                return render(request, "hr/login.html", {
                "message": "HR Account not valid here"
            })
        else:
            return render(request, "hr/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "hr/login_candidate.html")
    
@login_required
def candidate_test_window(request):
    current_user = request.user
    obj = TEST_CREDENTIALS.objects.get(candidate_id=current_user)

    resume = obj.resume_id
    job_description = obj.resume_id.jd_id.job_description

    resume_details = {
        'resume_score': resume.resume_score,
        'resume_rank': resume.resume_rank,
        'resume_level': str(resume.resume_level),  # Convert choice to human-readable value
        'resume_summary': resume.resume_summary
    }
    if request.method == 'POST':
        questions_json = request.session.get('questions')
        
        user_answers = [request.POST.get(f'question_{i}') for i in range(len(questions_json))]
        correct_answers = [question['correct'] for question in questions_json]
        
        score = sum(user_answer == str(correct_answer) for user_answer, correct_answer in zip(user_answers, correct_answers))
        score = float((score * 100)/ len(correct_answers))
        
        # Clear the stored questions from the session
        del request.session['questions']

        obj.test_taken = True
        obj.score = score
        obj.save()

        
        
        return HttpResponse(f'Your Score is {score} out of 10')
    else:
        # Generate questions here and store them in the session

        if obj.test_taken==True:
            return render(request,'hr/candidate_test.html',{
            'obj':resume_details,
            'job_description':job_description,
            'test_taken':'True'
        })
        else:
            questions_json = generate_questions(job_description=job_description)
            request.session['questions'] = questions_json
            
            return render(request,'hr/candidate_test.html',{
                'obj':resume_details,
                'job_description':job_description,
                'questions_json':questions_json
            })
    

    

    

