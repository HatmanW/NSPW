from django.db import models

class Cart(models.Model):
    item_name = models.CharField(max_length=30)
    item_size = models.DecimalField(max_length=3)

