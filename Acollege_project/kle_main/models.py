from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.expressions import F
from django.utils.html import escape, mark_safe

from PIL import Image
from PIL.Image import core as _imaging

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    is_student = models.BooleanField(default=False, null=True, blank=True)
    is_teacher = models.BooleanField(default=False, null=True, blank=True)
    is_library = models.BooleanField(default=False, null=True, blank=True)
    is_hod     = models.BooleanField(default=False, null=True, blank=True)

    # def __str__(self):
    #     return str(username) or ''

# blog ka part hai 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


# book request ke liye library wala
class request_book(models.Model):
    fullname= models.CharField(max_length=100)
    email= models.EmailField()
    subject= models.CharField(max_length=50)
    book_name= models.CharField(max_length=200)
    book_author_name= models.CharField(max_length=200)
    book_edition=models.CharField(max_length=200)
    additional_info=models.CharField(max_length=500)

    def __str__(self):
        return self.fullname
