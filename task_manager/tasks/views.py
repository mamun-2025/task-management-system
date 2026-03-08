from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout



def signup_view(request):
   if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request, user)
         return redirect('login')
   else: 
      form = SignUpForm()

   return render(request, 'tasks/signup.html', {'form': form})

def login_view(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
         user = form.get_user()
         login(request, user)
         return redirect('login')
   else:
      form = AuthenticationForm()
   return render(request, 'tasks/login.html', {'form': form })

def logout_view(request):
   if request.method == 'POST':
      logout(request)
      return redirect('login')
   
   
