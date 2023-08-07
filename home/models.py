from django.db import models

# Create your models here.


class register(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    targetprice = models.FloatField()
    link = models.TextField()

    def __str__(self):
        return self.name
