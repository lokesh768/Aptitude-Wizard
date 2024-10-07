from django.urls import path

from .views import *

urlpatterns = [
    path("",Home,name="home"),
    path("quantitative-aptitude/",Quantitative_Aptitude,name="quantitative-aptitude"),
    path("logical-reasoning/",Logical_Reasoning,name="logical-reasoning"),
    path("quantitative-aptitude/<str:category>/",Questions,name="questions"),
    path("logical-reasoning/<str:category>/",Questions,name="questions"),
    path("add-question/",AddQuestions,name="add-questions"),
    path("login/",login_page,name="login-page"),
    path("register/",register_page,name="register-page"),
    path("logout/",logout_page,name="logout-page"),
]

