from django.urls import path
from pinjam_buku.views import *
from book.views import *

app_name = 'pinjam_buku'

urlpatterns =[
    path('daftar_peminjaman/', show_borrow, name='daftar_peminjaman'),
    path('pinjam/<int:id>/', pinjam_buku, name='pinjam_buku'),
    path('get-books/', get_books_json, name='get_books_json'),
    path("kembalikan/<int:id>/", kembalikan_buku, name="kembalikan_buku"),
    path('pinjam_buku_ajax/<int:id>/', pinjam_buku_ajax, name='pinjam_buku_ajax'),
    path('pinjam_buku_flutter/<int:id>/', pinjam_buku_flutter, name='pinjam_buku_flutter'),
    path("kembalikan_flutter/<int:id>/<str:username>", kembalikan_buku_flutter, name="kembalikan_buku_flutter"),

]
