from django.db import models

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    discription = models.TextField()
    image = models.CharField(max_length=300)