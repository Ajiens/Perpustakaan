import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import UserWithRole
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def register(request):
  form = CustomUserCreationForm()
  
  if request.method == "POST":
      form = CustomUserCreationForm(request.POST)
      if form.is_valid():
          user = form.save()
          print()
          profile = UserWithRole(user=user, name=user.username, role=form.cleaned_data['role'])
          profile.save()
          messages.success(request, 'Your account has been successfully created')
          return redirect('authentication:login')
  
  context = {'form':form}
  return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
  if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      print("AA")
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user) 
          print("BBB")
          response = HttpResponseRedirect(reverse("Homepage:show_homepage")) 
          response.set_cookie('last_login', str(datetime.datetime.now())) 
          return response
      else:
          print("ADMINNN")
          messages.info(request, 'Username atau Password salah!')
  context = {}
  return render(request, 'login.html', context)

@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('authentication:login'))
    response.delete_cookie('last_login')
    return response