from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=15,blank=False)
    last_name = models.CharField(max_length=15,blank=False)   
    budget = models.IntegerField(blank=False)
    budget_left = models.DecimalField(max_digits=10000, decimal_places=2, blank=True)

class Expense(models.Model):
    title = models.CharField(max_length=50,blank=False)
    image_url = models.URLField(blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10000, decimal_places=2, blank=False)
    fk = models.ForeignKey(Profile, on_delete=models.CASCADE)