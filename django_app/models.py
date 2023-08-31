from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length = 100)
    date = models.DateField()
    money = models.IntegerField()
