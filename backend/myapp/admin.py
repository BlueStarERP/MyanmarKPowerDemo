from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Warehouse)
admin.site.register(StaffPermission)
admin.site.register(Category)
admin.site.register(Items)
admin.site.register(ItmColor)
admin.site.register(ItmSize)