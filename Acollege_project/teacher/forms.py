from django import forms
from .models import attendance,performance_update

class attendance_Form(forms.ModelForm):
    class Meta:
        model= attendance
        fields = "__all__" 
        # fields= ["stu_user","subject","Teacher","from_d","to_d","total_c","attended_c","remark","posted_d"]

class performance_update_form(forms.ModelForm):
    class Meta:
        model=performance_update
        fields = "__all__"