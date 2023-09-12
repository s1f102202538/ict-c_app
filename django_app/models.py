from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass

class dayregister(models.Model):
    user = models.ForeignKey(
        CustomUser,  # カスタムユーザーモデルを使用
        on_delete=models.CASCADE,
    )
    date_1 = models.DateTimeField()  
    date_2 = models.DateTimeField()  
    date_3 = models.DateTimeField()  
    amount = models.PositiveIntegerField() #データ型を変更

    def __str__(self):
        return f"Booking on {self.date_1}, {self.date_2}, {self.date_3}"