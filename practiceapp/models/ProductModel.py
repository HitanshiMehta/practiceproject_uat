from django.db import models

class ProductModel(models.Model):
    ProdcutId=models.AutoField(primary_key=True,db_column="Product Id")
    ProdcutName = models.CharField(max_length=100, db_column="Product Name")
    ProdcutPrice = models.IntegerField(db_column="Product Price")
