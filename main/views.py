from main.models import *
from main.serializers import *
from rest_framework import generics
from django.shortcuts import get_object_or_404


class OptionsList(generics.ListCreateAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer

class OptionTypeList(generics.ListCreateAPIView):
    queryset = OptionType.objects.all()
    serializer_class = OptionTypeSerializer

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

class OptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer

class OptionTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OptionType.objects.all()
    serializer_class = OptionTypeSerializer

    def get_object(self):
    	# Allows multiple fields lookup and case insensitive filter
	    queryset = self.get_queryset()
	    filter = {k+'__icontains':v for k,v in self.kwargs.items() if v}
	    obj = get_object_or_404(queryset, **filter)
	    self.check_object_permissions(self.request, obj)
	    return obj

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def get_object(self):
    	# Allows multiple fields lookup and case insensitive filter
	    queryset = self.get_queryset()
	    filter = {k+'__icontains':v for k,v in self.kwargs.items() if v}
	    obj = get_object_or_404(queryset, **filter)
	    self.check_object_permissions(self.request, obj)
	    return obj

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    
    def get_object(self):
    	# Allows multiple fields lookup and case insensitive filter
	    queryset = self.get_queryset()
	    filter = {k+'__icontains':v for k,v in self.kwargs.items() if v}
	    obj = get_object_or_404(queryset, **filter)
	    self.check_object_permissions(self.request, obj)
	    return obj

class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

