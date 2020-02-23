from django.db import models

class Article(models.Model):
    id=models.AutoField(primary_key=True,db_column="Id")
    title = models.CharField(max_length=120,db_column="Title")
    description = models.CharField(max_length=100,db_column="Description")
    body = models.CharField(max_length=100,db_column="Body")