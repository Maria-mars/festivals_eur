from django.db import models

from django.core.validators import RegexValidator

from apps.events.models import Events

PHONE_REGEX = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class Sponsor(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Name Sponsor')
    last_name = models.CharField(max_length=20, verbose_name=' Last Name')
    telephone = models.CharField(validators=[PHONE_REGEX], max_length=17, null=True, unique=True,
                                 verbose_name='Phone number')
    email = models.EmailField(max_length=150, null=True, unique=True, verbose_name='Email')
    description = models.TextField(max_length=200, null=True, verbose_name='Description')
    events = models.ForeignKey(Events, on_delete=models.CASCADE, verbose_name='Events')

    def __str__(self):
        return self.first_name + self.last_name


    def __str__(self):
        return self.description
