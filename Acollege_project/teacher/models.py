from django.db import models
from django.utils import timezone
from kle_main.models import User
# Create your models here.
class attendance(models.Model):
    stu_user = models.ForeignKey(User, on_delete=models.CASCADE,default=None,blank=True)
    subject=models.CharField(max_length=100,default=None, blank=True,null=True)
    Teacher=models.CharField(max_length=100,default=None, blank=True,null=True)
    from_d= models.DateField()
    to_d = models.DateField()
    total_c = models.IntegerField()
    attended_c = models.IntegerField()
    remark = models.CharField(max_length=500)
    posted_d = models.CharField(max_length=100)

    def __str__(self):
        return str(self.posted_d)

class performance_update(models.Model):
    stu_name = models.ForeignKey(User,on_delete=models.CASCADE,default=None,blank=True)
    subject = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    exam_name = models.CharField(max_length=100)
    other_exam = models.CharField(max_length=100)
    total_m = models.CharField(max_length=100)
    obtained_m = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    posted_d = models.CharField(max_length=100)

    def __str__(self):
        return str(self.posted_d)