from django.urls import path
from deskripsi_buku.views import *

app_name = 'deskripsi_buku'

urlpatterns =[
    path('', show_main, name='show_main'),
    path("daftar-buku-json/", show_json, name="get_books"),
    path('get_buku_json/', get_buku_json, name='get_buku_json'),
    path('get_buku_by_id', get_buku_json_by_id, name='get_buku_json_by_id'),
    path('deskripsi/<int:id>/', deskripsi_buku, name="deskripsi"),
    path('deskripsi_landingpage/<int:id>/', deskripsi_buku_landingpage, name="deskripsi_landingpage"),
    path('deskripsi/<int:id>/review/', review_buku, name="rating_buku"),
    path('deskripsi/add_review/', add_review_buku, name="add_review"),
    path('get_review/', get_review, name="get_review"),
    path('create-review-flutter/', add_review_flutter, name='create-review-flutter')
]