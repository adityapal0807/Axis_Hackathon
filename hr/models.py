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
    is_hr = models.BooleanField(default=True)
    visited = models.BooleanField(default=False)

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
    job_description = models.JSONField()
    recommendation_used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hr_id} - {self.jd_title} - {self.created_at}"

class Applied_resume(BaseFields):
    # hr_user= models.ForeignKey(Hr_data, on_delete=models.CASCADE)
    jd_id= models.ForeignKey(Job_Description, on_delete=models.CASCADE,related_name='jd_id')
    applicant_email= models.EmailField(null=True, blank=True)
    resume_score= models.FloatField(null=True, blank=True)
    resume_rank= models.IntegerField(null=True, blank=True)
    resume_level= models.CharField(max_length=100, choices=CHOICES_LEVEL)
    resume_summary= models.TextField(max_length=2000)
    resume_rank_reason= models.CharField(max_length= 1000, null= True, blank=True)
    resume_selected=models.BooleanField(default=False)
    def _str_(self):
        return f"{self.jd_id} - {self.applicant_email}"
    
class TEST_CREDENTIALS(BaseFields):
    candidate_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='candidate_id')
    resume_id = models.ForeignKey(Applied_resume,on_delete=models.CASCADE,related_name='applied_resume')
    test_taken = models.BooleanField(default=False)
    score = models.FloatField(null=True, blank=True)

class Chat(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.sender.username} to {self.receiver.username}: {self.content}'
