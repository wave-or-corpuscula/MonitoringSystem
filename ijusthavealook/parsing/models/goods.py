from django.db import models

from . import Categories


class Goods(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name
