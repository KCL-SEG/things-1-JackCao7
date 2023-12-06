from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Thing(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=30)
    description = models.TextField(max_length=120)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])