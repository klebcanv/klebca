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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
# from django.contrib.auth import views as auth_views
from kle_main import views
from kle_main import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index.as_view(),name='basepage'),
    path('kle_main/',include('kle_main.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', views.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('accounts/signup/Library/', views.LibraySignUpView.as_view(), name='library_signup'),
    path('accounts/signup/Hod/', views.HodSignUpView.as_view(), name='hod_signup'),
    path('accounts/changepassword/', views.user_change_pass, name='changepass'),

    # blog ka part hai
    path('profile/', user_views.profile, name='profile'),
    path('blog/',include('blog.urls')),
    path('api-blog/', include('blog.api.urls')),

    # chat ka part hai
    path('chat/',include('chat.urls')),

    # library ko include kar rahe hai 
    path('library/',include('library.urls')),

    # an hod maidam ka project include kar raheh hai 
    path('hod/',include('hod.urls')),

    # ab yahan hun teacher ko include kar rahe hai 
    path('teacher/',include('teacher.urls')),

    # ab yahan hum student ko include kar rahe hai
    path('student/',include('student.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    path('', include('blog.urls')),