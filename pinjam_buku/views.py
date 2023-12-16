import datetime
import json
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from authentication.models import UserWithRole
from pinjam_buku.models import Borrow
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

def show_borrow(request):
    user_id = request.COOKIES.get('user') #Ambil Cookie id
    role_user = User.objects.get(username=user_id)

    borrowed_books = Borrow.objects.filter(user=role_user)
    all_borrowed_books = [item.book for item in borrowed_books]
    return render(request, 'peminjaman.html', {'borrowed_books': all_borrowed_books})


def get_books_json(request):
    print()
    if request.user.is_authenticated:
        user = request.user
        print("kesini")
    else:
        user_id = request.COOKIES.get('user') #Ambil Cookie id
        user = User.objects.get(username=user_id)

    borrow_items = Borrow.objects.filter(user=user)
    borrowed_books = [item.book for item in borrow_items]
    context = [
        {
            'pk': book.pk,
            'title': book.title,
            'cover_link': book.cover_link,
            'author': book.author,
            'average_rating': book.average_rating,
            'lama_peminjaman': item.lama_peminjaman,
            'last_login' : request.COOKIES["last_login"][:-10] if "last_login" in request.COOKIES else "",
        }
        for book, item in zip(borrowed_books, borrow_items)
    ]
    return JsonResponse(context, safe=False)


def kembalikan_buku(request, id):
    user_id = request.COOKIES.get('user') #Ambil Cookie id
    role_user = User.objects.get(username=user_id)
    user = role_user

    book = get_object_or_404(Book, pk=id)
    borrowed_item = Borrow.objects.get(user=user, book=book, is_dikembalikan=False)
    borrowed_item.is_dikembalikan = True
    borrowed_item.delete()
    book.is_available = True
    book.save()
    success = True

    return JsonResponse({'success': success})

def pinjam_buku(request, id):
    user_id = request.COOKIES.get('user') #Ambil Cookie id
    role_user = User.objects.get(username=user_id)
    user = role_user

    book = get_object_or_404(Book, pk=id)
    if book.is_available:
        book_borrow_exists = Borrow.objects.filter(user=user, book=book).exists()
        if not book_borrow_exists:
            book_borrow = Borrow(user=user, book=book, is_dikembalikan=False)
            book_borrow.save()
            book.is_available = False
            book.save()
            success = True
        else:
            success = False
    else:
        success = False
    return JsonResponse({'success': success})

@csrf_exempt
def pinjam_buku_ajax(request,id):
    if request.method == 'POST':
        user_id = request.COOKIES.get('user') #Ambil Cookie id
        role_user = User.objects.get(username=user_id)
        user = role_user

        formData = request.POST
        lama_peminjaman = formData.get('lama_peminjaman')
        book = get_object_or_404(Book, pk=id)
        if book.is_available:
            book_borrow_exists = Borrow.objects.filter(user=user, book=book).exists()
            if not book_borrow_exists:
                book_borrow = Borrow(user=user, book=book,lama_peminjaman = lama_peminjaman, is_dikembalikan=False)
                book_borrow.save()
                book.is_available = False
                book.save()
            return HttpResponse(b"CREATED", status=201)
        else :
            return HttpResponseNotFound()
    return HttpResponseNotFound()


@csrf_exempt
def pinjam_buku_flutter(request,id):
    print("halo")
  
    if request.method == 'POST':
        print ("apakabar")
        data = json.loads(request.body)
        print("baik")
        user = request.COOKIES.get('user') 
        print(user)
        if (user == None):
            user = request.user
        print(user)
        print("ininih")
        lama_peminjaman = data['lama_peminjaman']
        book = get_object_or_404(Book, pk=id)
        if book.is_available:
            book_borrow_exists = Borrow.objects.filter(user=user, book=book).exists()
            if not book_borrow_exists:
                book_borrow = Borrow(user=user, book=book,lama_peminjaman = lama_peminjaman, is_dikembalikan=False)
                book_borrow.save()
                book.is_available = False
                book.save()
            return JsonResponse({"status": "success"}, status=200)
        else:
         return JsonResponse({"status": "error"}, status=401) 
    else:
        return JsonResponse({"status": "error"}, status=401)