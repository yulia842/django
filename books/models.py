from enum import Enum
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookType(Enum):
    ten_days = 1
    five_days = 2
    two_days = 3
 
class Book(models.Model):
    
    class BookType2(models.IntegerChoices):
        ten_days = 1, "Ten Days Loan"
        five_days = 2, "Five Days Loan"
        two_days = 3, "Two Days Loan"

    name = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200, null=False)
    year_published = models.DateField()
    type = models.SmallIntegerField(null=False, default = BookType2.two_days, choices=BookType2.choices)
    created_time=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, default='placeholder/')
    
    def __str__(self):
        return self.name

class Loan(models.Model):
    custID = models.ForeignKey(User, on_delete=models.CASCADE,)
    bookID = models.ForeignKey(Book, on_delete=models.CASCADE,)
    loan_date=models.DateTimeField()
    return_date=models.DateTimeField()



# https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-choices-enum-types