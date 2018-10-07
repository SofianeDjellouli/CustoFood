from rest_framework import serializers
from main.models import *
from collections import OrderedDict
from rest_framework.relations import PKOnlyObject

# class do(serializers.SlugRelatedField):
#     def to_representation(self, obj):
#         dict={}
#         dict[obj.optiontype]=[a for a in OptionType.objects.get(optiontype=obj).options.values_list('option', flat=True)]
#         return str(dict)


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

  def to_representation(self, instance):
    # Object instance -> Dict of primitive datatypes.
    ret = OrderedDict()
    fields = self._readable_fields
    for field in fields:
      try:
        attribute = field.get_attribute(instance)
      except SkipField:
        continue

      # We skip `to_representation` for `None` values so that fields do
      # not have to explicitly deal with that case.
      #
      # For related fields with `use_pk_only_optimization` we need to
      # resolve the pk value.
      check_for_none = attribute.pk if isinstance(
          attribute, PKOnlyObject) else attribute
      if check_for_none is None:
        ret[field.field_name] = None
      elif field.field_name == 'products':
        ret[field.field_name] = [[a, Products.objects.get(product=a).price]
                                 for a in field.to_representation(attribute)]
      elif field.field_name == 'optiontype':
        ret[field.field_name] = [{a: list(OptionType.objects.get(optiontype=a).options.values_list('option', flat=True))}
                                 for a in field.to_representation(attribute)]
      else:
        ret[field.field_name] = field.to_representation(attribute)

    return ret

  optiontype = serializers.SlugRelatedField(
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
