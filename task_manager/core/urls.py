
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin_security/', admin.site.urls),
    path('', include('tasks.urls')),
]
