# # from django.shortcuts import render

# # # Create your views here.
# # from django.views.decorators.csrf import csrf_exempt
# # from rest_framework.decorators import api_view, permission_classes
# # from rest_framework.permissions import AllowAny
# # from rest_framework.response import Response
# # from rest_framework.status import HTTP_200_OK

# # # Create your views here.
# # @csrf_exempt
# # @api_view(["GET"])
# # @permission_classes((AllowAny,))
# # def simpleapi(request):
# #     return Response({'text': 'Hello world, This is your first api call'},status=HTTP_200_OK)

# # # !!!!


# # from rest_framework import status
# # from rest_framework.decorators import api_view,permission_classes
# # from rest_framework.response import Response
# # from django.contrib.auth.forms import UserCreationForm

# # @api_view(['POST'])
# # @permission_classes((AllowAny,))
# # def signup(request):
# #     form = UserCreationForm(data=request.data)
# #     if form.is_valid():
# #         user = form.save()
# #         return Response("account created successfully", status=status.HTTP_201_CREATED)
# #     return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


# # # !!!!

# # from django.contrib.auth import authenticate
# # from django.views.decorators.csrf import csrf_exempt
# # from rest_framework.decorators import api_view, permission_classes
# # from rest_framework.permissions import AllowAny
# # from rest_framework.response import Response
# # from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
# # from rest_framework.authtoken.models import Token

# # @csrf_exempt
# # @api_view(["POST"])
# # @permission_classes((AllowAny,))
# # def login(request):
# #     username = request.data.get("username")
# #     password = request.data.get("password")
# #     if username is None or password is None:
# #         return Response({'error': 'Please provide both username and password'},
# #                         status=HTTP_400_BAD_REQUEST)
# #     user = authenticate(username=username, password=password)
# #     if not user:
# #         return Response({'error': 'Invalid Credentials'},
# #                         status=HTTP_404_NOT_FOUND)
# #     token, _ = Token.objects.get_or_create(user=user)
# #     return Response({'token': token.key},status=HTTP_200_OK)


# # # Classwork
# # @csrf_exempt
# # @api_view(["GET"])
# # @permission_classes((AllowAny,))
# # def productitem(request):
# #     products = [
# #         {
# #             "name": "Laptop",
# #             "price": 55000,
# #             "category": "Electronics"
# #         },
# #         {
# #             "name": "Mobile Phone",
# #             "price": 25000,
# #             "category": "Electronics"
# #         },
# #         {
# #             "name": "Chair",
# #             "price": 3000,
# #             "category": "Furniture"
# #         }
# #     ]
# #     return Response(products,status=HTTP_200_OK)

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# from rest_framework.status import (
#     HTTP_200_OK,
#     HTTP_400_BAD_REQUEST,
#     HTTP_404_NOT_FOUND,
# )

# # - SIMPLE API ----------------
# @csrf_exempt
# @api_view(["GET"])
# @permission_classes((AllowAny))
# def simpleapi(request):
#     return Response(
#         {'text': 'Hello world, This is your first api call'},
#         status=HTTP_200_OK
#     )

# # ---- SIGNUP API ----------------
# @api_view(['POST'])
# @permission_classes((AllowAny))
# def signup(request):
#     form = UserCreationForm(data=request.data)
#     if form.is_valid():
#         form.save()
#         return Response(
#             "account created successfully",
#             status=status.HTTP_201_CREATED
#         )
#     return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

# # ------------ LOGIN API ------
# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     if not username or not password:
#         return Response(
#             {'error': 'Please provide both username and password'},
#             status=HTTP_400_BAD_REQUEST
#         )

#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response(
#             {'error': 'Invalid Credentials'},
#             status=HTTP_404_NOT_FOUND
#         )

#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key}, status=HTTP_200_OK)

# # ------- PRODUCT API ------------
# @csrf_exempt
# @api_view(["GET"])
# @permission_classes((AllowAny))
# def productitem(request):
#     products = [
#         {"name": "Laptop", "price": 55000, "category": "Electronics"},
#         {"name": "Mobile Phone", "price": 25000, "category": "Electronics"},
#         {"name": "Chair", "price": 3000, "category": "Furniture"},
#     ]
#     return Response(products, status=HTTP_200_OK)
# # 
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import ProductSerializer

# @api_view(['POST'])
# def create_product(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # 
# from products.models import Product

# @api_view(['GET'])
# def list_products(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)
# # 
# from django.shortcuts import get_object_or_404

# @api_view(['PUT'])
# def update_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # 
# @api_view(['DELETE'])
# def delete_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     product.delete()
#     return Response({"message": "Product deleted"})


from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from products.forms import ProductForm
@api_view(['POST'])
@permission_classes((AllowAny,))
def create_product(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save()
        return Response({'id': product.id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)




from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view,permission_classes

@api_view(['GET'])
@permission_classes((AllowAny,))
def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)




from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from products.forms import ProductForm
from products.models import Product
from .serializers import ProductSerializer

@api_view(['PUT'])
@permission_classes((AllowAny,))
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.data, instance=product)
    if form.is_valid():
        form.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    



from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from rest_framework.permissions import AllowAny

@api_view(['DELETE'])
@permission_classes((AllowAny,))
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response("deleted successfully")     