from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, TaskForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import Task
from django.contrib.auth.decorators import login_required



# SignUp , Login and Logout Views 
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
         return redirect('task_list')
   else:
      form = AuthenticationForm()
   return render(request, 'tasks/login.html', {'form': form })

def logout_view(request):
      logout(request)
      return redirect('login')
   
   
# CRUD views for creating, reading, updating and deleting tasks
@login_required
def task_list(request):
   tasks = Task.objects.filter(user=request.user)
   return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
   if request.method == 'POST':
      form = TaskForm(request.POST)
      if form.is_valid():
         task = form.save(commit=False)
         task.user = request.user
         task.save()
         return redirect('task_list')
   else:
      form = TaskForm()
   return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
   task = get_object_or_404(Task, pk=pk, user=request.user)
   if request.method == 'POST':
      form = TaskForm(request.POST, instance=task)
      if form.is_valid():
         form.save()
         return redirect('task_list')
   else:
      form = TaskForm(instance=task)
   return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
   task = get_object_or_404(Task, pk=pk, user=request.user)
   if request.method == 'POST':
      task.delete()
      return redirect('task_list')
   return render(request, 'tasks/task_confirm_delete.html', {'task': task})


# Dashboard view to display 
@login_required
def dashboard_view(request):
   tasks = Task.objects.filter(user=request.user)

   #filter logic
   status_filter = request.GET.get('status')
   if status_filter in ['pending', 'completed']:
      tasks =tasks.filter(status=status_filter)
   
   priority_filter = request.GET.get('priority')
   if priority_filter in ['Low', 'Medium', 'High']:
      tasks = tasks.filter(priority=priority_filter)
      
   return render(request, 'tasks/dashboard.html', {'tasks': tasks })
