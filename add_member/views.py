from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from authentication.models import UserWithRole
from katalog_buku.models import Book
from .models import Favorit, UserProfile 
from .forms import UserProfileForm  
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

@login_required(login_url='/login')
def show_page(request):
    books = Book.objects.all()
    user_with_role = UserWithRole.objects.get(user=request.user)
    role = user_with_role.role

    context = {
        'name': request.user.username,
        'role': role,
        'books':books,
    }
    return render(request, 'profil.html', context)

def show_buku(request):

    books = Book.objects.all()

    context = {
        'books':books,
    }

    return render(request, 'show_buku.html', context)

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'userprofile/profil.html', {'user_profile': user_profile})


@csrf_exempt
def edit_profil_ajax(request):
    if request.method == 'POST':
        tl = request.POST.get('tanggal_lahir')

        if is_valid_date(tl)==False:
            return HttpResponseNotFound(404)
        
        
        desc = request.POST.get('description')
        
        name = request.user.username
        try:
            user_profile = UserProfile.objects.get(name=name)
            user_profile.delete()
        except:
            print('Gak ada')
        
        try:
            user_with_role = UserWithRole.objects.get(user=request.user)
        except:
            return HttpResponseRedirect(reverse('authentication:login'))
        role = user_with_role.role

        new_item = UserProfile(name=name, role=role, tanggal_lahir=tl, description=desc)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_profilUser_json(request):
    profil_user = UserProfile.objects.all()
    return HttpResponse(serializers.serialize('json', profil_user))

def get_user_profile_by_name(request):
    name = request.user.username
    try:
        user_profile = UserProfile.objects.get(name=name)
        print("UDAH ADAA")
        user_profile = [user_profile]
        return HttpResponse(serializers.serialize('json', user_profile))
    except:
        user_with_role = UserWithRole.objects.get(user=request.user)
        role = user_with_role.role
        user_profile = UserProfile(name=name, role=role, tanggal_lahir="", description="")
        user_profile.save()
        user_profile = [user_profile]
        print("BIKIN USER PROFILE BARU")
        return HttpResponse(serializers.serialize('json', user_profile))


def get_favorites(request):
    
    favorite_books = Favorit.objects.filter(user=request.user)
    
    return HttpResponse(serializers.serialize('json', favorite_books))
    

@csrf_exempt
def delete_favorit(request,id):
    if request.method == 'DELETE':
        data = Favorit.objects.get(pk=id)
        data.delete()

        return HttpResponse(b"DELETE", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def add_favorit(request, id):

    if request.method == 'POST':
        buku = Book.objects.get(pk=id)
        
        existing_favorit = Favorit.objects.filter(user=request.user, id_book=id_book).first()

        if existing_favorit:
            # Book with the same id_book already exists in Favorit
            
            return HttpResponse("Book is already in favorite list", status=201)
        
        print(buku.title)
        print(type(id))
    
        new_item = Favorit(user=request.user, id=id, title=buku.title, author=buku.author, number_of_pages=buku.number_of_pages, date_published=buku.date_published, publisher=buku.publisher)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


def is_valid_date(date_string):
    date_format = "%d/%m/%Y"
    try:
        # Attempt to parse the date using the provided format
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        # If parsing fails, it's not a valid date
        return False