from main.models import *
from main.serializers import *
from rest_framework import generics

class OptionsList(generics.ListCreateAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer

class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class CategoriesList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# class OptionsList(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Options.objects.all()
#     serializer_class = OptionsSerializer

# class ProductsList(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer

# class CategoriesList(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer

# class ChoiceList(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer

# class CartList(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

