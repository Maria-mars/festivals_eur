from django.db import models


class News(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name Post')
    date_pub = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=200, null=True, verbose_name='Description')

    def __str__(self):
        return self.name
