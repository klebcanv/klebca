from django.contrib import admin
from .models import attendance,performance_update


class attendance_admin(admin.ModelAdmin):
    list_display = ('stu_user','subject','Teacher','from_d','to_d','total_c','attended_c','remark','posted_d')
admin.site.register(attendance, attendance_admin)

class performance_update_admin(admin.ModelAdmin):
    list_display = ('stu_name','subject','teacher','exam_name','other_exam','total_m','obtained_m','remark','posted_d')
admin.site.register(performance_update,performance_update_admin)