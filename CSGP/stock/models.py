from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 50, blank=True, null=True)
    Name = models.CharField(max_length = 100, null=True)
    Current_Price = models.CharField(max_length= 150, blank=True, null=True)
    Debi = models.CharField(max_length= 150, blank=True, null=True)
    DungRak = models.CharField(max_length= 50, blank=True, null=True)
    Prev_Price = models.CharField(max_length= 150, blank=True, null=True)
    Trade_Volume = models.CharField(max_length= 150, blank=True, null=True)
    Trade_Money = models.CharField(max_length= 150, blank=True, null=True)
    Start_Price = models.CharField(max_length= 150, blank=True, null=True)
    High_Price = models.CharField(max_length= 150, blank=True, null=True)
    Low_Price = models.CharField(max_length= 150, blank=True, null=True)
    Week_52_High = models.CharField(max_length= 150, blank=True, null=True)
    Week_52_Low = models.CharField(max_length= 150, blank=True, null=True)
    UP_Price = models.CharField(max_length= 150, blank=True, null=True)
    Down_Price = models.CharField(max_length= 150, blank=True, null=True)
    Per = models.CharField(max_length= 150, blank=True, null=True)
    Amount = models.CharField(max_length= 200, blank=True, null=True)
    Face_Price = models.CharField(max_length= 100, blank=True, null=True)
    register_date = models.DateTimeField(default = timezone.now)

    

    def __str__(self):
        return self.Name