from django.db import models

from . import Goods, Observed


class Links(models.Model):
    good_id = models.ForeignKey(Goods, on_delete=models.DO_NOTHING)
    observed_id = models.ForeignKey(Observed, on_delete=models.DO_NOTHING)
    link = models.TextField()

    def __str__(self):
        return f'{self.good_id}: {self.link}'