from django.db import models


class Book(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    AuthorFirstName = models.CharField(max_length=100)
    AuthorLastName = models.CharField(max_length=100)
    Price = models.FloatField()
    Quantity = models.IntegerField()

    def __str__(self):
        return f"{self.Title} by {self.AuthorFirstName} {self.AuthorLastName}"
