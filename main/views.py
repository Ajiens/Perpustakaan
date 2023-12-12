import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from book.models import Book
from authentication.models import UserWithRole


# Create your views here.

def show_main(request):
    return render(request, "landingpage.html")

def show_pelanggan_page(request):
    return render(request,"main.html")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserWithRole(user=user, name=user.username, role="Pelanggan")
            profile.save()
            # pengunjung = Pengunjung(pengunjung=user, is_member=False) # TODO Definisikan pengunjung sesuai modelsnya
            # pengunjung.save() #Simpan pengunjung
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user.username, user)
            role_user = UserWithRole.objects.get(name=user.username)
            if (role_user.role == "Karyawan"):
                print("Karyawan")
                response = HttpResponseRedirect(reverse("katalog_buku:show_main_karyawan"))
                response.set_cookie('user', user)
                return response
            else:
                print("Pelanggan")
                response = HttpResponseRedirect(reverse("katalog_buku:show_main"))
                response.set_cookie('user', user)
                return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.delete_cookie('user')
    return response

def pelanggan_view(request):
    return render(request, 'pelanggan.html')

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_buku_json(request):
    books = Book.objects.values()  # Mengambil semua data buku dari database
    return JsonResponse(list(books), safe=False)  # Mengirimkan daftar buku sebagai JSON


def deskripsi_buku(request, id):
    book = Book.objects.values().get(pk=id)
    return render(request, 'deskripsi.html', {'book':book})

def get_buku_json_by_id(request, id):
    book = Book.objects.values().get(pk=id)
    return JsonResponse(book, safe=False)
