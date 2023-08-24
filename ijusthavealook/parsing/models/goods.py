from django.db import models

from . import Categories


class Goods(models.Model):
    name = models.CharField(max_length=255)
    cat = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
