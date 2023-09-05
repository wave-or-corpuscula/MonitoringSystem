from django.db import models


class Observed(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
    
# class Companies(models.Model):
#     name = models.CharField(max_length=255)
#     link = models.CharField(max_length=255)