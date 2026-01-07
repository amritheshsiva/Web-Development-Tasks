from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.employee_directory, name="employee_directory"),
]
