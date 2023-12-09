from django.db import models
from django.contrib.auth.models import User
from book.models import Book
# Create your models here.

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_dikembalikan = models.BooleanField(default=False)