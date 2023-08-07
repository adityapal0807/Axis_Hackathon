from django.db import models
from django.contrib.auth.models import AbstractUser

CHOICES_LEVEL=[
        ('beginner', "Beginner"),
        ('intermediate', "Intermediate"),
        ('advanced', "Advanced")
    ]

# Create your models here
class User(AbstractUser):
    employer_id= models.CharField(max_length=25, null=True, blank=True)
    employer_name= models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=20,null=True,blank=True)

    def _str_(self):
        return f"{self.employer_name} - {self.employer_id}"

class BaseFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Job_Description(BaseFields):
    hr_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='hr_id')
    jd_title= models.CharField(max_length= 100, null=True)
    job_description = models.TextField(max_length=5000)
    recommendation_used = models.BooleanField(default=False)

    def _str_(self):
        return f"{self.hr_id} - {self.jd_title}"

class Applied_resume(BaseFields):
    # hr_user= models.ForeignKey(Hr_data, on_delete=models.CASCADE)
    jd_id= models.ForeignKey(Job_Description, on_delete=models.CASCADE,related_name='jd_id')
    resume_text= models.TextField(max_length=2000)
    applicant_email= models.EmailField(null=True, blank=True)
    resume_score= models.IntegerField(null=True, blank=True)
    resume_rank= models.IntegerField(null=True, blank=True)
    resume_level= models.CharField(max_length=100, choices=CHOICES_LEVEL)
    resume_summary= models.TextField(max_length=2000)
    resume_rank_reason= models.CharField(max_length= 1000, null= True, blank=True)
    resume_selected=models.BooleanField(default=False)
    def _str_(self):
        return f"{self.jd_name} - {self.applicant_email}"

class Application_status(BaseFields):
    unique_application_id= models.ForeignKey(Applied_resume, on_delete=models.CASCADE,related_name='app_no')
    CHOICES=[
        ('not_selected',"Not Selected"), ('taken', "Test Taken"), ('not_taken', "Not taken")
    ]
    test_status= models.CharField(max_length=100, choices=CHOICES)
    test_score= models.IntegerField(null=True, blank= True)
    applicant_selected= models.BooleanField(default=False)
    # id pass if selected
    applicant_id= models.IntegerField(null=True, blank=True)
    # pass will be same as id
    def _str_(self):
        return f"{self.unique_application_id}, {self.applicant_selected}"
    
class Chat_History(BaseFields):
    pass
    
