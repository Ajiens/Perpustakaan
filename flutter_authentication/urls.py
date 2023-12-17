from django.urls import path
from flutter_authentication.views import login, logout, register

app_name = 'flutter_authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register')
]