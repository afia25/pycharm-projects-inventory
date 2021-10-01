from django.db import models

class Inventory_admin(models.Model):
    inv_admin_id = models.IntegerField(primary_key=True)
    inv_admin_name = models.TextField()
    inv_admin_email = models.CharField(max_length=30)


