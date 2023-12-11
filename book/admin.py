from django.contrib import admin

from .models import Book

from deskripsi_buku.models import Review
from add_wishlist.models import WishlistItem
from pinjam_buku.models import Borrow
from authentication.models import UserWithRole

myModels = [Book, Review, WishlistItem, Borrow, UserWithRole]  # iterable list
admin.site.register(myModels)
# Register your models here.
