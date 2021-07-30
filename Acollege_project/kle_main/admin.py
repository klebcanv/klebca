from django.contrib import admin
from .models import User,Profile

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
 list_display = ('id','username','is_student','is_teacher','is_library','is_hod','password')

# blog ka part hai
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    list_filter = ('user', )
    list_per_page = 20

admin.site.register(Profile, ProfileAdmin)


# book request library wala
from .models import request_book

class request_book_admin(admin.ModelAdmin):
    list_display = ('id','fullname','email','subject','book_name','book_author_name' ,'book_edition' ,'additional_info')

admin.site.register(request_book,request_book_admin)
