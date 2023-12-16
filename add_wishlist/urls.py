from django.urls import path
from add_wishlist.views import *
from book.views import *

app_name = 'wishlist'

urlpatterns =[
    path("", wishlist_view, name='wishlist'),
    path("add/<int:book_id>/", add_to_wishlist, name="add"),
    path("remove/<int:book_id>/", remove_from_wishlist, name="remove"),
    path("get-books/", get_books_json, name='get_books_json'),
    path("add-flutter/<int:book_id>/", add_to_wishlist_flutter, name="add_flutter")
]