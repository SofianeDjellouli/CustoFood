from main.models import *
from main.serializers import *
from rest_framework import generics

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

    # def list(self,request):
    # 	print(self.request.META)
    # 	queryset = self.get_queryset()
    #     serializer = CategoriesSerializer(queryset, many=True)
    #     return Response(serializer.data)
        
    

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

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

