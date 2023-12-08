from django.db import models
from django.contrib.auth.models import User
from book.models import Book
# Create your models here.

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    tanggal_peminjaman = models.DateField(auto_now_add=True)
    tanggal_pengembalian = models.DateField()
    is_dikembalikan = models.BooleanField()
    nama = models.CharField(max_length=100)
    gambarBuku = models.TextField()
    title = models.CharField(max_length=200)
