from django.contrib import admin

from .models import CustomUser,UserType,UserDetailBuyer,UserDetailSupplier
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser,UserAdmin)
admin.site.register(UserType)
admin.site.register(UserDetailBuyer)
admin.site.register(UserDetailSupplier)