from django.contrib import admin
from .models import Room, Message

# Register your models here.
# admin.site.register(Room)
# admin.site.register(Message)

class Roomadmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Room, Roomadmin)


class Messageadmin(admin.ModelAdmin):
    list_display = ('id', 'room' ,'user' ,'date' , 'value')
admin.site.register(Message, Messageadmin)