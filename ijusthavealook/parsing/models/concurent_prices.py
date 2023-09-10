from django.db import models

from . import ConcurentGoods, Observed


class ConcurentPrices(models.Model):
    good_id = models.ForeignKey(ConcurentGoods, on_delete=models.DO_NOTHING)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.good_id}, {self.price}'
