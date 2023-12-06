from django.urls import path
from katalog_buku.views import show_main, add_book, show_xml, show_json, show_xml_by_id, show_json_by_id, get_book_json, add_book_ajax

app_name = 'katalog_buku'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-book/', add_book, name='add_book'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('get-book/', get_book_json, name='get_book_json'),
    path('add_book_ajax/', add_book_ajax, name='add_book_ajax')
]