from django.contrib import admin
from apps.tickets.models import Tickets


@admin.register(Tickets)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['name','date', 'type']
    list_filter = ['name']