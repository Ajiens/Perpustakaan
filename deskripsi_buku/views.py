import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import JsonResponse

from django.contrib.auth.models import User
from book.models import Book
from deskripsi_buku.models import Review

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_main(request):
    return render(request, "mainmain.html")

def get_buku_json(request):
    books = Book.objects.values()  # Mengambil semua data buku dari database
    return JsonResponse(list(books), safe=False)  # Mengirimkan daftar buku sebagai JSON

def deskripsi_buku(request, id):
    book = Book.objects.values().get(pk=id)
    return render(request, 'deskripsi.html', {'book':book})

def deskripsi_buku_landingpage(request,id):
    book = Book.objects.values().get(pk=id)
    return render(request, 'deskripsi_landingpage.html', {'book':book})

def review_buku(request, id):
    book = Book.objects.values().get(pk=id)
    review = Review.objects.values().all()
    context = {
        'book':book,
        'reviews': list(review),
    }
    return render(request, 'review.html', context)

@csrf_exempt
def add_review_flutter(request):
    if request.method == 'POST':
        # Ambil data JSON dari body request
        data = json.loads(request.body)

        # Dapatkan nilai rating dan komentar dari data JSON
        rating = data.get('rating')
        komentar = data.get('komentar')
        username = data.get('username')

        user = User.objects.get(username=username)
        print(user)
        # user = request.COOKIES.get('user') #Ambil Cookie id
        # if (user == None):
        #     user = request.user

        if (int(rating) > 5):
            return JsonResponse({"status": "error"}, status=401)
        
        buku_id = int(data.get("buku_id"))

        try:
            book = Book.objects.get(pk=buku_id)
        except Book.DoesNotExist:
            return JsonResponse({"status": "error"}, status=401)

        if int(rating) == 5:
            book.five_star_ratings += 1
        elif int(rating) == 4:
            book.four_star_ratings += 1
        elif int(rating) == 3:
            book.three_star_ratings += 1
        elif int(rating) == 2:
            book.two_star_ratings += 1
        elif int(rating) == 1:
            book.one_star_ratings += 1
        else:
            messages.error(request, 'Rating tidak boleh lebih dari 5.')

        new_rating = ((book.average_rating * book.rating_count) + int(rating)) / (book.rating_count + 1)
        book.average_rating = round(new_rating, 2)
        book.rating_count += 1
        book.save()

        new_review = Review(book=book, user=user, rating_user=rating, komentar=komentar)
        new_review.save()
        print(new_review)
    
        return JsonResponse({"status": "success"}, status=200)

    return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def add_review_buku(request):
    if request.method == 'POST':
        komentar = request.POST.get("komentar")
        rating = request.POST.get("rating")
        if (int(rating) > 5):
            messages.error(request, 'Rating tidak boleh lebih dari 5.')
        
        user_id = request.COOKIES.get('user') #Ambil Cookie id
        user = User.objects.get(username=user_id)
        print(user)
        buku_id = int(request.POST.get("buku_id"))

        try:
            book = Book.objects.get(pk=buku_id)
        except Book.DoesNotExist:
            messages.error(request, 'Anda harus login terlebih dahulu sebelum menambahkan review')
            return redirect('main:login')

        if int(rating) == 5:
            book.five_star_ratings += 1
        elif int(rating) == 4:
            book.four_star_ratings += 1
        elif int(rating) == 3:
            book.three_star_ratings += 1
        elif int(rating) == 2:
            book.two_star_ratings += 1
        elif int(rating) == 1:
            book.one_star_ratings += 1
        else:
            messages.error(request, 'Rating tidak boleh lebih dari 5.')

        if (len(komentar) != 0):
            book.review_count += 1
        new_rating = ((book.average_rating * book.rating_count) + int(rating)) / (book.rating_count + 1)
        book.average_rating = round(new_rating, 2)
        book.rating_count += 1
        book.save()

        new_review = Review.objects.create(book=book, user=user, rating_user=rating, komentar=komentar)
        # new_review = Review(book=book, user=user, rating_user=rating, komentar=komentar)
        # print(new_review)
        # new_review.save()

        return HttpResponse('Review berhasil ditambahkan', status=201)
    else:
        return HttpResponseForbidden()


def get_review(request):
    # review = Review.objects.values()
    review = Review.objects.values()
    return JsonResponse(list(review), safe=False)
    # return HttpResponse(serializers.serialize("json", review), content_type="application/json")


def get_buku_json_by_id(request):
    book = Book.objects.values().get(pk=int(request.GET.get("book_id")))
    # print("Inidia nih si buku ID:",book)
    # return HttpResponse(serializers.serialize("json", book), content_type="application/json")
    return JsonResponse(book, safe=False)

# Untuk ngambil semua data di database

