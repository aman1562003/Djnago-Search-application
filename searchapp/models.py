from django.db import models

class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    aggregate_rating = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    prize = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
