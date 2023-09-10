from django.db import models

from . import Goods, Observed


class ConcurentGoods(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Observed, on_delete=models.DO_NOTHING)
    origin_good_id = models.ForeignKey(Goods, on_delete=models.DO_NOTHING, null=True)
    link = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.__class__}, {self.name}, {self.origin_good_id}"


