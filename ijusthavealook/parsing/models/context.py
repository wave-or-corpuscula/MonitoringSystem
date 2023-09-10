from django.db import models

from . import Observed


class Context(models.Model):
    our_company = models.ForeignKey(Observed, on_delete=models.DO_NOTHING)
