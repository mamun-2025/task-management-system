from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, TaskForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import Task
from django.contrib.auth.decorators import login_required

# DRF token authentication & permissions imports 
from .serializers import TaskSerializer
from rest_framework.authtoken.models import Token 
from django.contrib.auth import authenticate 
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status



# Login api for token authentication
@api_view(['POST'])
@permission_classes([AllowAny]) # Don't take token for login
def api_login(request):
   username = request.data.get('username')
   password = request.data.get('password')
   user = authenticate(username=username, password=password)

   if user:
      token, _ = Token.objects.get_or_create(user=user)
      return Response({'token': token.key})
   return Response({'error': 'Invalid credentials'}, status=400)




# HTML CRUD views for Task model and user authentication views for signup, login and logout
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








## Django REST Framework API views for Task model to allow CRUD operations via API endpoints 
## CRUD APIs protected with token authentication and only accessible to authenticated users 

# ✅ Task List API
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # Only authenticated users can access 
def api_task_list(request):
   tasks = Task.objects.filter(user=request.user)
   serializer = TaskSerializer(tasks, many=True)
   return Response(serializer.data)

# ✅ Task Detail API
@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def api_task_detail(request, pk):
   task = get_object_or_404(Task, pk=pk, user=request.user)
   serializer = TaskSerializer(task)
   return Response(serializer.data)

# ✅ Task Create API
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_task_create(request):
   serializer = TaskSerializer(data=request.data)
   if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Task Update API
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_task_update(request, pk):
   task = get_object_or_404(Task, pk=pk, user=request.user)
   serializer = TaskSerializer(instance=task, data=request.data)
   if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
   return Response(serializer.errors , status=status.HTTP_404_BAD_REQUEST)

# ✅ Task Delete API
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_task_delete(request, pk):
   task = get_object_or_404(Task, pk=pk, user=request.user)
   task.delete()
   return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

   
