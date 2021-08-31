from django.db import models
from django.utils import timezone


class Tickets(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    date = models.DateTimeField(auto_now=True, blank=True)
    type = models.CharField(max_length=150, verbose_name='Type')

    def __str__(self):
        return self.name
