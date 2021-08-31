from django.contrib import admin
from apps.organizers.models import Organizer


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ['last_name']
