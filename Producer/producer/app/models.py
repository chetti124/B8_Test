from django.db import models

# Create your models here.

class Product(models.Model):
    name =models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        db_table = "product"
