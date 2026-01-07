from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", views.student_list, name="student_list"),
]
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.student_list, name="home"),      # 👈 added
    path("students/", views.student_list, name="student_list"),
]
