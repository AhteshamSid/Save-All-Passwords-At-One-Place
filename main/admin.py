from django.contrib import admin
from .models import User, SavePassword

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'pwd']

class SavePasswordAdmin(admin.ModelAdmin):
    list_display = ['user','title', 'url', 'pwd', 'hide_pwd']


admin.site.register(User, UserAdmin)
admin.site.register(SavePassword, SavePasswordAdmin)