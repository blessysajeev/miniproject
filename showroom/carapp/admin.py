from django.contrib import admin
from email.headerregistry import Group
from django.contrib import admin
from.models import Vehicles
from django.contrib.auth.models import Group,User
 # Register your models here.
class VehicleAdmin(admin.ModelAdmin):
     list_display=['name','price','available','created','updated']
     list_editable=['price','available']
     list_per_page=20
    # prepopulated_fields={'slug':('name',)}
admin.site.register(Vehicles,VehicleAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
