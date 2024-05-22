from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Expenses(models.Model):
    description = models.CharField(max_length=100)
    amount = models.IntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(1000000)]
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class MonthlyIncome(models.Model):
    amount = models.IntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(100000000)]
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Default(models.Model):
    amount = models.IntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(100000000)]
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
