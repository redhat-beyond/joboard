from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from accounts.models import UserAccount

admin.site.register(UserAccount)


class AccountInline(admin.StackedInline):
    model = UserAccount
    can_delete = False
    verbose_name = 'user account'
    verbose_name_plural = 'user accounts'


class UserAdmin(BaseUserAdmin):
    inlines = (AccountInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
