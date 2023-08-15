from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("dashboard", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('dashboard/jd_description',views.jd_description_analyser,name='jd_description_analyser'),
    path("analyse_resumes", views.analyse_resumes, name="analyse_resumes"),
    path("resume_rankings", views.ranked_resumes, name="resume_rankings"),
    path('JDProgress/<str:jd_id>',views.JD_Progress,name='jd_progress'),

    # API ROUTES
    path('api/analyse_jd',views.analyse_js_api,name='analyse_jd'),

    #candidate
    path('candidate',views.candidate_login,name='candidate_login'),
    path('candidate/test',views.candidate_test_window,name='candidate_test_window'),
    path('candidate/candidate_audio',views.candidate_audio,name='candidate_audio'),
    path('transcribe_audio',views.transcribe,name='transcribe')
]
