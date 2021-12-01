from django.contrib import admin

from .models import CustomUser,UserType,T002Parents,T003Childminder
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserChangeForm,UserCreationForm

#管理者サイトのユーザ追加項目
@admin.register(CustomUser)
class AdminUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('last_name', 'first_name', 'last_name_kana', 'first_name_kana', 'email', 'sex', 'birthday', 'postal_code', 'address', 'tel','userType')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('email','password1','password2'),
        }),
    )
    list_display = ('get_full_name', 'get_full_name_kana', 'email', 'sex', 'birthday', 'postal_code', 'address','tel', 'is_staff',)
    search_fields = ('username', 'email',)
    ordering = ('date_joined',)
    filter_horizontal = ('groups', 'user_permissions',)
    

    admin.site.register(UserType)
    admin.site.register(T002Parents)
    admin.site.register(T003Childminder)
