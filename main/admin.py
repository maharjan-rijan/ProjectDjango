from django.contrib import admin
from main.models import *
# Register your models here.
admin.site.site_header = "Chandragiri Municipality"
admin.site.index_title = "Chandragiri Municipality"

class AboutAdmin(admin.ModelAdmin):
    list_display=('title','slug','contact','email','description')
class MemberAdmin(admin.ModelAdmin):
    list_display=('name','slug','category','image','designation','contact','email','position')

admin.site.register(About,AboutAdmin)
admin.site.register(Member,MemberAdmin)