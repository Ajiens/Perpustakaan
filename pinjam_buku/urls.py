from django.urls import path
from pinjam_buku.views import *
from book.views import *

app_name = 'pinjam_buku'

urlpatterns =[
    path('show-peminjaman/', show_peminjaman, name='show_peminjaman'),
    path('get-pinjem/', get_pinjam_json, name='get_pinjam_json'),
    path('get-buku-item/', get_buku_json, name='get_buku_json'),
    path('pinjam_buku/', pinjam_buku, name='pinjam_buku'),
    path('get-buku-by-id/<int:id>/', get_buku_by_id, name='get_buku_by_id'),
    path('kembalikan-buku/<int:id>/', kembalikan_buku, name='kembalikan_buku'),
    path('get-objek-by-id/<int:id>/', get_objek_by_id, name='get_objek_by_id'),
]
