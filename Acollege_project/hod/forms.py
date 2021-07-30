# contact request from contact us page se hod page tak
from django import forms
from .models import contact_request,stu_feedback,parents_feedback,stf_feedback


class contact_request_Form(forms.ModelForm):
    class Meta:
        model= contact_request
        fields= ["yourname", "youremail", "subject", "yourmessage"]



class stu_feedback_form(forms.ModelForm):
    class Meta:
        model = stu_feedback
        fields = ["username","email","fd1","fd2","fd3","fd4","fd5","fd6","fd7"]


class parents_feedback_form(forms.ModelForm):
    class Meta:
        model = parents_feedback
        fields = ["stu_name","par_relation","par_name","par_ph_no","par_email","par1","par2","par3","par4","par5","par6","par7"]


class stf_feedback_form(forms.ModelForm):
    class Meta:
        model = stf_feedback
        fields = ["name","email","stf1","stf2","stf3","stf4","stf5","stf6","stf7"]