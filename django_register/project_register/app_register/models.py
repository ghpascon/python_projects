from django.db import models

class product_info(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.TextField(max_length=255)
    product_color = models.TextField(max_length=255)
    product_size = models.TextField(max_length=255)
    product_amount = models.IntegerField()
