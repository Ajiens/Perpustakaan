from django.urls import path
from flutter_authentication.views import login, logout, register

app_name = 'flutter_authentication'

urlpatterns = [
    path('login_flutter/', login, name='login'),
    path('logout_flutter/', logout, name='logout'),
    path('register_flutter/', register, name='register')
]