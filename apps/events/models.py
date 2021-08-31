from django.db import models
from django.utils import timezone
from location_field.models.plain import PlainLocationField

from apps.tickets.models import Tickets


class Events(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name Event')
    date_start = models.DateTimeField(auto_now=True)
    date_end = models.DateTimeField(auto_now=True)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    description = models.TextField(max_length=200, null=True, verbose_name='Description')
    tickets = models.ForeignKey(Tickets, on_delete=models.CASCADE, verbose_name='Tickets')

    def __str__(self):
        return self.name
