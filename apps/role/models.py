from django.db import models

from apps.events.models import Events


class Role(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    description = models.CharField(max_length=150, verbose_name='Description')
    events = models.ForeignKey(Events, on_delete=models.CASCADE, verbose_name='Events')

    def __str__(self):
        return self.name
