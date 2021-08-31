from django.db import models
from apps.events.models import Events


class Organizer(models.Model):
    last_name = models.CharField(max_length=150, verbose_name='Last Name')
    first_name = models.CharField(max_length=150, verbose_name='First Name')
    events = models.ForeignKey(Events, on_delete=models.CASCADE, verbose_name='Events')

    def __str__(self):
        return self.first_name + self.last_name
