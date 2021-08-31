from django.contrib import admin
from apps.sponsor.models import Sponsor


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','telephone', 'email', 'description']
    list_filter = ['first_name', 'last_name']
