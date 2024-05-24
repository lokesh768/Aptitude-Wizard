"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from aptitudewizard.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
