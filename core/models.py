from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    pageCount = models.IntegerField()
    # publishedDate = models.DateField()
    # shortDescription = models.CharField(max_length=250)
    # longDescription = models.CharField(max_length=250)
    categories = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.title} - {self.author}"


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    history = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.user} - {self.history}"


class MyBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.CharField(max_length=255)
