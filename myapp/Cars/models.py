from django.db import models

class Specs(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    weight = models.PositiveIntegerField()