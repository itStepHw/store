from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    rating = models.FloatField()
    created_at = models.DateTimeField()



