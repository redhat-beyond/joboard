from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from accounts.models import UserAccount
from .forms import SignUpForm, AccountForm


admin.site.register(UserAccount)


class AccountInline(admin.StackedInline):
    model = UserAccount
    form = AccountForm
    can_delete = False
    verbose_name = 'user account'
    verbose_name_plural = 'user accounts'


class UserAdmin(BaseUserAdmin):
    add_form = SignUpForm
    inlines = (AccountInline,)
    list_display = ('username',
                    'email',
                    'first_name',
                    'last_name',
                    'is_active')


UserAdmin.add_form = SignUpForm
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',)
    }),
)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
