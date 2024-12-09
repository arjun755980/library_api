from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    available_copies = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    membership_type = models.CharField(max_length=50, choices = [('Regular','Regular'),('Premium', 'Premium')])
    registered_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nameself