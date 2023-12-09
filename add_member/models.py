from django.db import models
from django.contrib.auth.models import User

from katalog_buku.models import Book

class UserProfile(models.Model):
    
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    tanggal_lahir = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)

    
class Favorit(models.Model) :
    title = models.TextField(null=True, blank=True)
    id = models.IntegerField(primary_key=True, blank=True)
    author = models.TextField(null=True, blank=True)
    number_of_pages = models.IntegerField(null=True, blank=True)
    date_published = models.TextField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)