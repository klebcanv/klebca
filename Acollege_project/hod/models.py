from django.db import models
from django.db.models import manager

# Create your models here.
# contact request contactus page se hod page tak wala
class contact_request(models.Model):
    yourname= models.CharField(max_length=100)
    youremail= models.EmailField()
    subject= models.CharField(max_length=50)
    yourmessage= models.CharField(max_length=200)

    def __str__(self):
        return self.yourname


class stu_feedback(models.Model):
    username= models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    fd1 = models.CharField(max_length=20)
    fd2 = models.CharField(max_length=20)
    fd3 = models.CharField(max_length=20)
    fd4 = models.CharField(max_length=20)
    fd5 = models.CharField(max_length=20)
    fd6 = models.CharField(max_length=20)
    fd7 = models.CharField(max_length=500)

    def __str__(self):
        return self.fd1

class parents_feedback(models.Model):
    stu_name=models.CharField(max_length=50)
    par_relation=models.CharField(max_length=200)
    par_name=models.CharField(max_length=50)
    par_ph_no=models.CharField(max_length=10)
    par_email=models.CharField(max_length=200)
    par1=models.CharField(max_length=20)
    par2=models.CharField(max_length=20)
    par3=models.CharField(max_length=20)
    par4=models.CharField(max_length=20)
    par5=models.CharField(max_length=20)
    par6=models.CharField(max_length=20)
    par7=models.CharField(max_length=500)

    def __str__(self):
        return self.stu_name



class stf_feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    stf1 = models.CharField(max_length=20)
    stf2 = models.CharField(max_length=20)
    stf3 = models.CharField(max_length=20)
    stf4 = models.CharField(max_length=20)
    stf5 = models.CharField(max_length=20)
    stf6 = models.CharField(max_length=20)
    stf7 = models.CharField(max_length=500)

    def __str__(self):
        return self.name