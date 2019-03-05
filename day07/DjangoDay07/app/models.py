from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=255)
    price = models.IntegerField()
    detail = models.CharField(max_length=255)

    class Meta:
        db_table = 'goods'
