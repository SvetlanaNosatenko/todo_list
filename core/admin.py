from django.contrib import admin
from core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("username", "email", "first_name", "last_name")
    exclude = ['password']
    readonly_fields = ("last_login", "date_joined")




