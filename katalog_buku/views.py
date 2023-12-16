from django.shortcuts import render
from django.http import HttpResponseRedirect
from katalog_buku.forms import BookForm
from book.models import Book
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from authentication.models import UserWithRole
import json
from django.http import JsonResponse


# Create your views here.

def show_main(request):
    print("pengunjung main2")
    books = Book.objects.all()

    context = {
        'books': books,
    }

    # main = "";
    # if class pelanggan {
    #   main = main1.html
    # }
    # else if class karyawan {
    #   main = main2.html
    # }

    return render(request, "main1.html", context)

def show_main_karyawan(request):
    print("Pekerja Main1")
    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, "main2.html", context)


def add_book(request):
    form = BookForm(request.POST or None)

    # if form.is_valid() and request.method == "POST":
    #     form.save()
    #     return HttpResponseRedirect(reverse('katalog_buku:show_main'))

    # context = {'form': form}
    return render(request, "add_book.html")


def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_book_json(request):
    book_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book_item))

@login_required(login_url='/login')
@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        user_id = request.COOKIES.get('user') #Ambil Cookie id
        role_user = UserWithRole.objects.get(user=user_id)

        if (role_user.role != "Pelanggan"):
            title = request.POST.get("title")
            cover_link = request.POST.get("cover_link")
            author = request.POST.get("author")
            harga = int(request.POST.get("harga"))

            # Pastikan semua fields Books keisi, jangan sampe null. Karena bisa ngerusak database
            new_book = Book(title=title, cover_link=cover_link, author=author, harga=harga, rating_count=0, review_count=0, average_rating=0.0, five_star_ratings=0, four_star_ratings=0, three_star_ratings=0,two_star_ratings=0,one_star_ratings=0, number_of_pages=0, date_published="",publisher="",isbn=0,description="")
            new_book.save()

            return HttpResponse(b"CREATED", status=201)
        else:
            return HttpResponse(b"Access denied", status=401)



@csrf_exempt
def add_book_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Book.objects.create( 
            #user = request.user,
            title = data["title"],
            cover_link = data["cover link"],
            author = data["author"],
            harga = int(data["price"]),
            rating_count = 0,
            review_count = 0,
            average_rating=0, 
            five_star_ratings=0, 
            four_star_ratings=0, 
            three_star_ratings=0,
            two_star_ratings=0,
            one_star_ratings=0, 
            number_of_pages=0, 
            date_published="",
            publisher="",
            isbn=0,
            description="",
            is_available = True,
        )

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)