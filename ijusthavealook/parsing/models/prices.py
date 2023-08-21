from django.db import models
from datetime import datetime

from parsing.models.goods import Goods
from parsing.models.observed import Observed


class Prices(models.Model):
    good_id = models.ForeignKey(Goods, on_delete=models.DO_NOTHING)
    observed_id = models.ForeignKey(Observed, on_delete=models.DO_NOTHING)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.good_id}, {self.observed_id}: {self.price}'
