from django.contrib import admin
from programProject.models import *
# Register your models here.
class ProgramProjectAdmin(admin.ModelAdmin):
    list_display=('title','slug','file','dateTime','category')

admin.site.register(ProgramProject,ProgramProjectAdmin)