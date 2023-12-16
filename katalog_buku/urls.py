from django.urls import path
from katalog_buku.views import show_main, show_main_karyawan,add_book, show_xml, show_json, show_xml_by_id, show_json_by_id, get_book_json, add_book_ajax
from katalog_buku.views import add_book_flutter

app_name = 'katalog_buku'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('karyawan/', show_main_karyawan, name='show_main_karyawan'),
    path('add-book/', add_book, name='add_book'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('get-book/', get_book_json, name='get_book_json'),
    path('add-book-ajax/', add_book_ajax, name='add_book_ajax'),
    path('add-flutter/', add_book_flutter, name='add_book_flutter'),
]