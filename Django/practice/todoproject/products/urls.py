# from django.urls import path
# from . import views

# urlpatterns = [
#     path(
#         'send_product_email/<int:pk>/',
#         views.send_product_email,
#         name='send_product_email'
#     ),
# ]

from django.urls import path
from . import views
urlpatterns = [
    
    path('create_product', views.create_product, name='createproductapi'),
]