from django.urls import path
from add_member import views
from add_member.views import add_favorit, get_profilUser_json, show_buku, show_page
from add_member.views import show_page
from add_member.views import edit_profil_ajax, get_favorites, delete_favorit, get_user_profile_by_name


app_name = 'add_member'

urlpatterns = [
    path('', show_page, name='show_page'),
    path('get_product/', get_profilUser_json, name='get_profilUser_json'),
    path('edit_profil_ajax/', edit_profil_ajax, name='edit_profil_ajax'),
    path('add_favorit/<int:id_book>/', add_favorit, name='add_favorit'),
    path('get_favorites/', get_favorites, name='get_favorites'),
    path('get_user_profile_by_name/',get_user_profile_by_name, name='get_user_profile_by_name'),
    path('delete_favorit/<int:id>/', delete_favorit, name = 'delete_favorit'),
]