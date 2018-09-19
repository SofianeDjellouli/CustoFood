from django.db import models
from django.contrib.auth.models import User

class Options(models.Model):
    option = models.CharField(max_length=100)
    # category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.option

class Products(models.Model):
    product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product

class Categories(models.Model):
    category = models.CharField(max_length=100)
    options = models.ManyToManyField(Options)
    products = models.ManyToManyField(Products)

    def __str__(self):
        return self.name

class Choice(models.Model):
	options = models.ManyToManyField(Options)
	product = models.ForeignKey(Products, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return '{} {} {}'.format(self.quantity, self.product, self.options)

class Cart(models.Model):
	choices = models.ManyToManyField(Choice)
	client = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return '{} {}'.format(self.client, self.choices)