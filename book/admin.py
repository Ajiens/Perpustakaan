from django.contrib import admin

from .models import Book
from deskripsi_buku.models import Review
from authentication.models import UserWithRole
myModels = [Book, Review, UserWithRole]  # iterable list
admin.site.register(myModels)
# Register your models here.
