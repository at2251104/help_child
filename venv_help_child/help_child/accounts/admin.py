from django.contrib import admin
<<<<<<< HEAD

from .models import CustomUser,UserType,UserDetailBuyer,UserDetailSupplier

=======
from .models import CustomUser,UserType,UserDetailBuyer,UserDetailSupplier
>>>>>>> e4e64d6c113e395f5ce1f9feb680d0d7e5478c2c
admin.site.register(CustomUser)
admin.site.register(UserType)
admin.site.register(UserDetailBuyer)
admin.site.register(UserDetailSupplier)