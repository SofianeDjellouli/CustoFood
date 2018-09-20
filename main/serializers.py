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
    options = serializers.SlugRelatedField(
        many=True,
        queryset=Options.objects.all(),
        slug_field='option'
    )
    product = serializers.SlugRelatedField(
        queryset=Products.objects.all(),
        slug_field='product'
    )

    class Meta:
        model = Choice
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='client'
    )
    choices = serializers.SlugRelatedField(
        queryset=Choice.objects.all(),
        slug_field='product'
    )
    class Meta:
        model = Cart
        fields = '__all__'
