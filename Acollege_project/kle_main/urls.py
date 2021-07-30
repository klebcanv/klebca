"""Acollege_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url,include
from . import views

app_name = 'kle_main'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('page_not_found/',views.page_not_found.as_view(),name="page_not_found"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('about_us/',views.about_us.as_view(),name="about_us"),
    path('digital_library/',views.digital_library,name="digital_library"),
    path('passing_criteria/',views.passing_criteria.as_view(),name="passing_criteria"),  
    path('admission_details/',views.admission_details.as_view(),name="admission_details"), 
    path('student_apply/',views.student_apply.as_view(),name="student_apply"),
    path('about_web/',views.about_web.as_view(),name="about_web"), 
]
