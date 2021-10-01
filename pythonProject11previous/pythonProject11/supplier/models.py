from django.db import models

class Supplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=40)
    supplier_email = models.CharField(max_length=30)
    supplier_contact=models.CharField(max_length=11)







