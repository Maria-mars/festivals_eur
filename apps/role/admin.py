from django.contrib import admin
from apps.role.models import Role


@admin.register(Role)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ['name']
