from django.contrib import admin
from .models import User,Job_Description,Applied_resume
# Register your models here.
admin.site.register(User)
@admin.register(Job_Description)
class JobDescriptionAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at', 'hr_id', 'job_description', 'recommendation_used')

admin.site.register(Applied_resume)