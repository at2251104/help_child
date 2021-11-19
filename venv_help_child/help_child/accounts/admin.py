from django.contrib import admin
from .models import CustomUser,UserType,UserDetailBuyer,UserDetailSupplier

admin.site.register(CustomUser)
admin.site.register(UserType)
admin.site.register(UserDetailBuyer)
admin.site.register(UserDetailSupplier)