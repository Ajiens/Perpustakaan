"""
URL configuration for perpustakaan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from add_wishlist.views import *

urlpatterns = [
    path('', include("main.urls")),
    path('katalog_buku/', include('katalog_buku.urls')),
    path('admin/', admin.site.urls),
    path("api/books/", include("book.urls")),
    path("deskripsi_buku/", include("deskripsi_buku.urls")),
    path("wishlist/", include("add_wishlist.urls")),
    path("add_member/",include("add_member.urls")),
    path('auth/', include('flutter_authentication.urls')),
]
