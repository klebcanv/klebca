from teacher.forms import attendance_Form,performance_update_form
from django.shortcuts import render
from django.views.generic.base import TemplateView
from kle_main.models import User
from django.contrib import messages
from django.shortcuts import redirect
from .models import attendance
from .models import performance_update as performance_updateModel

# Create your views here.
class attandance_update(TemplateView):
  template_name = 'attendance.html'
  def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(**kwargs)
      nn = User.objects.all()
      context = {'nn':nn}
      return context

class performance_update(TemplateView):
    template_name= 'performance.html'
    def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(**kwargs)
      nn = User.objects.all()
      context = {'nn':nn}
      return context

class task_update(TemplateView):
    template_name='task.html'

def at_form(request,username):
    name = User.objects.get(username=username)
    nn = User.objects.all()
    current_user = request.user
    att = attendance.objects.all()
    if request.method == "POST":
        a_form = attendance_Form(request.POST)
        if a_form.is_valid():
            a_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('attandance_update')
        else:
            messages.success(request,"your form is not valid")
    else:
        a_form = attendance_Form()
    context = {'nn':nn,'name':name, 'a_form':a_form,'att':att,'current_user':current_user}
    return render(request, 'att_form.html', context)

def per_form(request,username):
    name = User.objects.get(username=username)
    nn = User.objects.all()
    current_user = request.user
    per = performance_updateModel.objects.all()
    if request.method == "POST":
        a_form = performance_update_form(request.POST)
        if a_form.is_valid():
            a_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('performance_update')
        else:
            messages.success(request,"your form is not valid")
    else:
        a_form = performance_update_form()
    context = {'nn':nn,'name':name, 'a_form':a_form,'per':per,'current_user':current_user}
    return render(request, 'per_form.html', context)