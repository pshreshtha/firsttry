from django.db import models


class Inventory(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    stock = models.IntegerField(default=0)

