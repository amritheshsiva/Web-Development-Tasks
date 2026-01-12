from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/all/', views.all_customers, name='all_customers'),
    path('customers/filtered/', views.filtered_customers, name='filtered_customers'),
]
