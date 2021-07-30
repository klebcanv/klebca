from django.contrib import admin

# Register your models here.
# contact request contact us se hod tak
from .models import contact_request,stu_feedback,parents_feedback,stf_feedback

class contact_request_admin(admin.ModelAdmin):
    list_display = ('id','yourname','youremail','subject','yourmessage')

admin.site.register(contact_request,contact_request_admin)



class stu_feedback_admin(admin.ModelAdmin):
    list_display = ('id','username','email','fd1','fd2','fd3','fd4','fd5','fd6','fd7')
admin.site.register(stu_feedback,stu_feedback_admin)

class parents_feedback_admin(admin.ModelAdmin):
    list_display = ('id','stu_name','par_relation','par_name','par_ph_no','par_email','par1','par2','par3','par4','par5','par6','par7')
admin.site.register(parents_feedback,parents_feedback_admin)

class stf_feedback_admin(admin.ModelAdmin):
    list_display = ('id','name','email','stf1','stf2','stf3','stf4','stf5','stf6','stf7')
admin.site.register(stf_feedback,stf_feedback_admin)