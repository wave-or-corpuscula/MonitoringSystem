from django.db import models

from . import Categories, Observed


class Goods(models.Model):
    name = models.CharField(max_length=255)
    observed_id = models.ForeignKey(Observed, on_delete=models.DO_NOTHING)
    link = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name
