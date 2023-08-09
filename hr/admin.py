from django.contrib import admin
from .models import User,Job_Description,Applied_resume,TEST_CREDENTIALS,Chat
# Register your models here.
admin.site.register(User)
admin.site.register(Job_Description)
admin.site.register(Applied_resume)
admin.site.register(TEST_CREDENTIALS)
admin.site.register(Chat)
# admin.site.register(Application_status)