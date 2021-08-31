from django.contrib import admin
from apps.promotions.models import Promotions


@admin.register(Promotions)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'url']
    list_filter = ['name']
