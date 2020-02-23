from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    end_date=models.DateField()
    owner = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.title)