import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from authentication.models import UserWithRole
from django.core import serializers
from katalog_buku.models import Book
from django.contrib.auth.models import User

# Create your views here.
list_of_karyawan = ['admin1','admin2'] #contoh 

@login_required(login_url='/authentication/login/')
def show_main(request):
    try:
        user_with_role = UserWithRole.objects.get(user=request.user)
    except:
        return HttpResponseRedirect(reverse('authentication:login'))
    role = user_with_role.role
    if(request.user.username in list_of_karyawan):
        role = 'Admin'
        
    context = {
        'name': request.user.username,
        'role': role,
    }

    return render(request, "main.html", context)

@login_required(login_url='/authentication/login/')
def show_user(request):
    if(request.user.username not in list_of_karyawan):
        return HttpResponseNotFound()
    context = {

    }
    return render(request, "show_user_admin.html", context) #part 1 fix

def show_main_karyawan(request):
    context = {

    }
    return render(request, "main_karyawan.html", context)

@login_required(login_url='/authentication/login/')
def show_list_of_books(request):
    context={

    }
    return render(request, "show_list_of_books.html", context)

def show_list_of_books_karyawan(request):
    context={

    }
    return render(request, "show_list_of_books_karyawan.html", context) #part 2

def get_books(request):
    books = Book.objects.all()

    return HttpResponse(serializers.serialize('json', books))

def get_user(request):
    users = UserWithRole.objects.exclude(name__in=list_of_karyawan)

    return HttpResponse(serializers.serialize('json', users))

def get_user_with_role_by_name(request):
    name = request.user.username
    
    user_with_role = UserWithRole.objects.get(name=name)
    user_with_role = [user_with_role]

    return HttpResponse(serializers.serialize('json', user_with_role))
    
        