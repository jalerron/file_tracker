from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'full_name']
