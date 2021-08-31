from django.contrib import admin
from apps.events.models import Events


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_start', 'date_end', 'location', 'description']
    list_filter = ['name']
