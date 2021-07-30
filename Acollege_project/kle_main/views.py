from django.shortcuts import render
from django.views.generic import View,TemplateView

from django.views.generic import TemplateView
from .models import User
from .forms import StudentSignUpForm,TeacherSignUpForm,librarySignUpForm,hodSignUpForm,UserUpdateForm, ProfileUpdateForm
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth import login,authenticate, logout, update_session_auth_hash
from django.shortcuts import redirect,render, HttpResponseRedirect

from .decorators import student_required,teacher_required,library_required,hod_required,all_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib import messages

# Create your views here.

class index(TemplateView):
    template_name = 'kle_main/002index.html'

class stu_stf_login(TemplateView):
    template_name = 'kle_main/008login.html'

class page_not_found(TemplateView):
    template_name = 'kle_main/009page_not_found.html'

# class contact_us(TemplateView):
#     template_name = 'kle_main/004contact_us.html'

# contact us wala from contact us se hod tak
from hod.forms import contact_request_Form
# @method_decorator([login_required, all_required], name='dispatch')
def contact_us(request):
    form= contact_request_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        print('found an error')

    context= {'form': form }
    return render(request, 'kle_main/004contact_us.html', context)

class about_us(TemplateView):
    template_name = 'kle_main/003about_us.html'

# request form wala 
from .forms import request_book_Form
# @method_decorator([login_required, all_required], name='dispatch')
def digital_library(request):
    form= request_book_Form(request.POST or None)
    if form.is_valid():
        form.save()
        # return redirect('/')
    else:
        print('found an error')

    context= {'form': form }
    return render(request, 'kle_main/005digital_library.html', context)


class passing_criteria(TemplateView):
    template_name = 'kle_main/006passing_criteria.html'

class about_web(TemplateView):
    template_name = 'kle_main/011about_web.html'

class admission_details(TemplateView):
    template_name = 'kle_main/007admission_details.html'

class student_apply(TemplateView):
    template_name = 'kle_main/0010student_apply.html/'

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

@method_decorator([login_required, hod_required], name='dispatch')
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

def QuizListView(request):
    return render(request,"/")



@method_decorator([login_required, hod_required], name='dispatch')
class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

def QuizListView(request):
    return render(request,"/")



@method_decorator([login_required, hod_required], name='dispatch')
class LibraySignUpView(CreateView):
    model = User
    form_class = librarySignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'library'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

def QuizListView(request):
    return render(request,"/")



@method_decorator([login_required, hod_required], name='dispatch')
class HodSignUpView(CreateView):
    model = User
    form_class = hodSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'hod'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

def QuizListView(request):
    return render(request,"/")


def user_change_pass(request):
  if request.user.is_authenticated:
    if request.method == "POST":
      fm = PasswordChangeForm(user=request.user, data=request.POST)
      if fm.is_valid():
        fm.save()
        update_session_auth_hash(request, fm.user)
        return HttpResponseRedirect('/')
    else:
      fm = PasswordChangeForm(user=request.user)
    return render(request, 'registration/changepass.html', {'form':fm})
  else:
    return HttpResponseRedirect('/accounts/login//')

# ye sab blog ka part hai 
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'registration/profile.html', context)