from .models import GoldUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import GoldUserCreationForm, GoldUserChangeForm

class GoldUserAdmin(UserAdmin):
    model = GoldUser
    form = GoldUserChangeForm
    add_form = GoldUserCreationForm

    readonly_fields = ('username','password','first_name','last_name','email',
			'gender','goldWeight')
    list_display = ('username', 'accountNumber','is_staff', 'is_active','gender',)
    list_filter = ('username', 'is_staff', 'is_active','gender',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',
			'email','gender','goldWeight')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser', 'groups', 'user_permissions',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','first_name','last_name', 'password1', 'password2', 'is_staff', 'is_active','gender',)}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(GoldUser, GoldUserAdmin)

