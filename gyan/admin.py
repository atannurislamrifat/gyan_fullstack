from django.contrib import admin
from gyan.models import form,contact_from

# Register your models here.
class formAdmin(admin.ModelAdmin):
 list_display=('id','tid','f_name','l_name','number','mail','msg')
admin.site.register(form,formAdmin)

class formAdmin(admin.ModelAdmin):
 list_display=('name','email','subject','message')
admin.site.register(contact_from,formAdmin)
