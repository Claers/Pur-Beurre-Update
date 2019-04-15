"""Used to register models into admin view
"""

from django.contrib import admin
from .models import Product, Category, Favorite, Profile
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Profile)
