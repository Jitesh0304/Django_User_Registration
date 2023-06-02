from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class UserModelAdmin(UserAdmin):

    list_display= ('id','email', 'username','otp','is_admin','is_verified')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email','password','is_verified')}),
        ('Personal info', {'fields': ('username',)}),
        ("Permissions", {'fields':('is_admin',)}),
        )

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields' : ('email','username', 'password1', 'password2'),
        })
    )
    search_fields = ('email',)
    ordering = ('id','email', 'created_at')
    filter_horizontal = ()
         
        
admin.site.register(User, UserModelAdmin)
