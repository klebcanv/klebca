from kle_main.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import TemplateView
from .models import contact_request as contact_requestModel
from .models import stu_feedback as stu_feedbackModel
from .models import parents_feedback as parents_feedbackModel
from .models import stf_feedback as stf_feedbackModel
from .forms import parents_feedback_form, stu_feedback_form,stf_feedback_form
class contact_request(TemplateView):
  template_name = 'hod/contact_request.html'
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    stud = contact_requestModel.objects.all()
    context = {'stu':stud}
    return context

  
class home_all_feedback(TemplateView):
  template_name = 'hod/home_all_feedback.html'
  def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(**kwargs)
      stud = stu_feedbackModel.objects.all()
      pare = parents_feedbackModel.objects.all()
      stf = stf_feedbackModel.objects.all()
      context = {'stu':stud,'para':pare,'stf':stf}
      return context
 
  

def student_feedback(request):
    form= stu_feedback_form(request.POST or None)
    if form.is_valid():
        obj = form.save()
        user = request.user.get_username()
        obj.username = user
        obj.save()
        return redirect('/')
    else:
        print('found an error')

    context= {'form': form }
    return render(request, 'hod/001student_feedback.html', context)



# class parents_feedback(TemplateView):
#   template_name = 'hod/002parents_feedback.html'
def parents_feedback(request):
    form= parents_feedback_form(request.POST or None)
    if form.is_valid():
        obj2 = form.save()
        user = request.user.get_username()
        obj2.stu_name = user
        obj2.save()
        # form.save()
        return redirect('/')
    else:
        print('found an error')

    context= {'form': form }
    return render(request, 'hod/002parents_feedback.html', context)

# class staff_feedback(TemplateView):
#   template_name = 'hod/003staff_feedback.html'
def staff_feedback(request):
    form= stf_feedback_form(request.POST or None)
    if form.is_valid():
        obj3 = form.save()
        user = request.user.get_username()
        obj3.name = user
        obj3.save()
        # form.save()
        return redirect('/')
    else:
        print('found an error')

    context= {'form': form }
    return render(request, 'hod/003staff_feedback.html', context)