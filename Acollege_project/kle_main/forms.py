from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from .models import User,Profile

class TeacherSignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'college Email'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user


class StudentSignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'college Email'}

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user

class librarySignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'college Email'}

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_library = True
        user.save()
        return user

class hodSignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'college Email'}

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_hod = True
        user.save()
        return user

# blog ka part hai 
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']




# book request ke liye library wala
from .models import request_book
class request_book_Form(forms.ModelForm):
    class Meta:
        model= request_book
        fields= ["fullname", "email", "subject", "book_name" , "book_author_name" , "book_edition" , "additional_info"]