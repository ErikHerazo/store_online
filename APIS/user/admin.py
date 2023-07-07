from django.contrib import admin

from .models import ModelUser

@admin.register(ModelUser)
class ModelUserAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'username', 'email'

    class Meta:
        db_table = 'store_users'
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'