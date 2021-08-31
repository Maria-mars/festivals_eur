from django.db import models

# Create your models here.
from django.utils import timezone

from apps.events.models import Events


class Promotions(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name Event')
    date_start = models.DateTimeField(auto_now=True)
    date_end = models.DateTimeField(auto_now=True, blank=True)
    description = models.TextField(max_length=200, null=True, verbose_name='Description')
    url = models.SlugField(unique=True, default='')
    events = models.ForeignKey(Events, on_delete=models.CASCADE, verbose_name='Events')

    def __str__(self):
        return self.name

