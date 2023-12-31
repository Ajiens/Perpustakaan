import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.models import User
from book.models import Book
from add_wishlist.models import WishlistItem

def add_to_wishlist(request, book_id):
    user_id = request.COOKIES.get('user') #Ambil Cookie id
    user = User.objects.get(username=user_id)
    
    book = get_object_or_404(Book, pk=book_id)
    keterangan = request.POST.get('keterangan')

    wishlist = WishlistItem(user=user, wished_book=book, keterangan=keterangan)
    wishlist_item_exists = WishlistItem.objects.filter(user=user, wished_book=book).exists()

    if wishlist_item_exists:
        success = False
    else:
        wishlist.save()
        success = True

    return JsonResponse({'success': success})


@csrf_exempt
def remove_from_wishlist(request, book_id):
    if request.user.is_authenticated: 
        user = request.user
    else:
        user_id = request.COOKIES.get('user')
        user = User.objects.get(username=user_id)

    book = get_object_or_404(Book, pk=book_id)

    wishlist_item = WishlistItem.objects.get(user=user, wished_book=book)
    wishlist_item.delete()
    success = True

    return JsonResponse({'success': success})


def wishlist_view(request):
    user_id = request.COOKIES.get('user') #Ambil Cookie id
    role_user = User.objects.get(username=user_id)

    wishlist_items = WishlistItem.objects.filter(user=role_user)  
    wished_books = [item.wished_book for item in wishlist_items]
    return render(request, 'wishlist.html', {'wishlist': wished_books})


def get_books_json(request):
    if request.user.is_authenticated: 
        user = request.user
    else:
        user_id = request.COOKIES.get('user')
        user = User.objects.get(username=user_id)

    wishlist_items = WishlistItem.objects.filter(user=user)
    wished_books = [item.wished_book for item in wishlist_items]
    books_data = [
        {
            'pk': book.pk,
            'title': book.title,
            'cover_link': book.cover_link,
            'author': book.author,
            'average_rating': book.average_rating,
            'harga': book.harga,
            'keterangan' : item.keterangan, # mengambil data keterangan dari models
        }
        for book, item in zip(wished_books, wishlist_items)
    ]
    return JsonResponse(books_data, safe=False)


@csrf_exempt
def add_to_wishlist_flutter(request, book_id):

    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        username = data.get('username')

        user = User.objects.get(username=username)

        book = get_object_or_404(Book, pk=book_id)
        keterangan = data['keterangan']

        wishlist = WishlistItem(user=user, wished_book=book, keterangan=keterangan)
        wishlist_item_exists = WishlistItem.objects.filter(user=user, wished_book=book).exists()

        print("letsgo")
        if wishlist_item_exists:
            return JsonResponse({"status": "error"}, status=401)
        else:
            wishlist = WishlistItem(user=user, wished_book=book, keterangan=keterangan)
            wishlist.save()
            return JsonResponse({"status": "success"}, status=200)

    else:
        return JsonResponse({"status": "error"}, status=401)