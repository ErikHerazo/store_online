from django.contrib import admin
from .models import OnlineStoreUsers
# Register your models here.

@admin.register(OnlineStoreUsers)
class OnlineStoreUsersAdmin(admin.ModelAdmin):
    list_display = 'username', 'password', 'full_name', 'identification_number', 'email'