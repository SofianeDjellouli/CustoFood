from django.contrib import admin
from .models import *

admin.site.register(OptionType)
admin.site.register(Options)
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Choice)
admin.site.register(Cart)

