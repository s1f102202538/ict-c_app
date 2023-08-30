from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    date1 = models.DateTimeField()
    date2 = models.DateTimeField()
    date3 = models.DateTimeField()
    money = models.IntegerField(blank=True, default=0)