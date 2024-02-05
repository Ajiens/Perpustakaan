import datetime
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from pinjam_buku.models import Borrow
from book.models import Book
from django.views.decorators.csrf import csrf_exempt

def show_json(request):
    data = Borrow.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_borrow(request):
    borrowed_books = Borrow.objects.filter(user=request.user)
    all_borrowed_books = [item.book for item in borrowed_books]
    return render(request, 'peminjaman.html', {'borrowed_books': all_borrowed_books})

def get_books_json(request):
    borrow_items = Borrow.objects.filter(user=request.user)
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
    user = request.user
    book = get_object_or_404(Book, pk=id)
    borrowed_item = Borrow.objects.get(user=user, book=book, is_dikembalikan=False)
    borrowed_item.is_dikembalikan = True
    borrowed_item.delete()
    book.is_available = True
    book.save()
    success = True

    return JsonResponse({'success': success})

def pinjam_buku(request, id):
    user = request.user
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
        formData = request.POST
        lama_peminjaman = formData.get('lama_peminjaman')
        book = get_object_or_404(Book, pk=id)
        if book.is_available:
            book_borrow_exists = Borrow.objects.filter(user=request.user, book=book).exists()
            if not book_borrow_exists:
                book_borrow = Borrow(user=request.user, book=book,lama_peminjaman = lama_peminjaman, is_dikembalikan=False)
                book_borrow.save()
                book.is_available = False
                book.save()
            return HttpResponse(b"CREATED", status=201)
        else :
            return HttpResponseNotFound()
    return HttpResponseNotFound()
