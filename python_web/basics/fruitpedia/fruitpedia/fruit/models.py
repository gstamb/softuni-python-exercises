from django.db import models

class FruitModel(models.Model):
    name = models.CharField(blank=False, max_length=30)
    image_url = models.URLField(blank=False)
    description = models.TextField(blank=False)
    nutrition = models.TextField(blank=True)