from django.db import models

class register_product(models.Model):
    product_id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    receive_method = models.CharField(max_length=50)

class get_email(models.Model):
    nome_user = models.TextField(max_length=255)
    email_user = models.TextField(max_length=255)
   