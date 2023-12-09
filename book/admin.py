from django.contrib import admin

from .models import Book

from deskripsi_buku.models import Review
from add_wishlist.models import WishlistItem
from pinjam_buku.models import Borrow

myModels = [Book, Review, WishlistItem, Borrow]  # iterable list
admin.site.register(myModels)
# Register your models here.
