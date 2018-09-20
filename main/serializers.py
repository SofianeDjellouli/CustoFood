from rest_framework import serializers
from main.models import *

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'        

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    options = serializers.SlugRelatedField(
        many=True,
        queryset=Options.objects.all(),
        slug_field='option'
    )
    products = serializers.SlugRelatedField(
        many=True,
        queryset=Products.objects.all(),
        slug_field='product'
    )

    class Meta:
        model = Categories
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
