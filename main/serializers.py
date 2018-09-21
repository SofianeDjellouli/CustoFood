from rest_framework import serializers
from main.models import *

class do(serializers.SlugRelatedField):
    def to_representation(self, obj):
        dict={}
        dict[obj.optiontype]=[a for a in OptionType.objects.get(optiontype=obj).options.values_list('option', flat=True)]
        return str(dict)

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'        

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class OptionTypeSerializer(serializers.ModelSerializer):
    options = serializers.SlugRelatedField(
        many=True,
        queryset=Options.objects.all(),
        slug_field='option'
    )

    class Meta:
        model = OptionType
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    optiontype = do(
        many=True,
        queryset=OptionType.objects.all(),
        slug_field='optiontype'
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
