
from django.urls import path
from .views import (
   signup_view,
   login_view, 
   logout_view,
   task_list,
   task_create,
   task_update,
   task_delete,
   dashboard_view,
   api_task_list,
   api_task_detail,
   api_task_create,
   api_task_update,
   api_task_delete,
   api_login,
 )


urlpatterns = [
    # Usr authentication views for signup, login and logout
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # HTML CRUD views for Task model
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('update/<int:pk>/', task_update, name='task_update'),
    path('delete/<int:pk>/', task_delete, name='task_delete'),
    path('dashboard/', dashboard_view, name='dashboard'),

    # Django REST Framework API views for Task model to allow CRUD operations via API endpoints
    path('api/tasks/', api_task_list, name='api_task_list'),
    path('api/tasks/<int:pk>/', api_task_detail, name='api_task_detail'),
    path('api/tasks/create/', api_task_create, name='api_task_create'),
    path('api/tasks/<int:pk>/update/', api_task_update, name='api_task_update'),
    path('api/tasks/<int:pk>/delete/', api_task_delete, name='api_task_delete'),

    # 1. Authentication API (Token-based login endpoint)
    path('api/login/', api_login, name='api_login'),

    # 2. Task CRUD APIs token authentication and only access users
    path('api/tasks/', api_task_list, name='api_task_list'),
    path('api/tasks/<int:pk>/', api_task_detail, name='api_task_detail'),
    path('api/tasks/create/', api_task_create, name='api_task_create'),
    path('api/tasks/<int:pk>/update/', api_task_update, name='api_task_update'),
    path('api/tasks/<int:pk>/delete/', api_task_delete, name='api_task_delete'),

]

