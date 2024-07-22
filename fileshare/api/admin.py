from django.contrib import admin
from .models import Profile, File

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','user_type']

admin.site.register(Profile,ProfileAdmin)

class FileAdmin(admin.ModelAdmin):
    list_display = ['uploader','file','uploaded_at']
admin.site.register(File,FileAdmin)
