from teacher.forms import attendance_Form
from django.shortcuts import render
from django.views.generic.base import TemplateView
from kle_main.models import User
from django.contrib import messages
from django.shortcuts import redirect
from teacher.models import attendance,performance_update


def attandance(request):
    att = attendance.objects.all()
    current_user = request.user
    # if (current_user == att.stu_user):
    #   att = attendance.objects.all()
    context = {'att':att,'current_user':current_user}
    return render(request,'stu_attendance.html' , context)

def performance(request):
    per = performance_update.objects.all()
    current_user = request.user
    # if (current_user == att.stu_user):
    #   att = attendance.objects.all()
    context = {'per':per,'current_user':current_user}
    return render(request,'stu_performance.html' , context)

class task(TemplateView):
    template_name='stu_task.html'

