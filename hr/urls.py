from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("dashboard", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("analyse_resumes", views.analyse_resumes, name="analyse_resumes"),

    # API ROUTES
    path('dashboard/jd_description',views.jd_description_analyser,name='jd_description_analyser')
]
