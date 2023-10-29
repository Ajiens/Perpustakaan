from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.core import serializers
from book.models import Book
from add_wishlist.models import WishlistItem

def add_to_wishlist(request, book_id):
    user = request.user
    book = get_object_or_404(Book, pk=book_id)

    wishlist = WishlistItem(user=user, wished_book=book)
    wishlist_item_exists = WishlistItem.objects.filter(user=user, wished_book=book).exists()

    if wishlist_item_exists:
        success = False
    else:
        wishlist.save()
        success = True

    return JsonResponse({'success': success})


def remove_from_wishlist(request, book_id):
    user = request.user
    book = get_object_or_404(Book, pk=book_id)

    wishlist_item = WishlistItem.objects.get(user=user, wished_book=book)
    wishlist_item.delete()
    success = True

    return JsonResponse({'success': success})



# def remove_from_wishlist(request, book_id):
#     wishlist = request.session.get('wishlist', [])
    
#     if book_id in wishlist:
#         wishlist.remove(book_id)
#         request.session['wishlist'] = wishlist
#         success = True
#     else:
#         success = False

#     return JsonResponse({'success': success})


def wishlist_view(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    wished_books = [item.wished_book for item in wishlist_items]
    return render(request, 'wishlist.html', {'wishlist': wished_books})


def get_books_json(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    wished_books = [item.wished_book for item in wishlist_items]
    books_data = [
        {
            'pk': book.pk,
            'title': book.title,
            'cover_link': book.cover_link,
            'author': book.author,
            'average_rating': book.average_rating,
            'harga': book.harga,
        }
        for book in wished_books
    ]
    return JsonResponse(books_data, safe=False)