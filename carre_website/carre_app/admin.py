from django.contrib import admin
from .models import Product, Collection, Comporter, Categorie, Subcategorie, TypeProduct
# Register your models here.
admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Comporter)
admin.site.register(Categorie)
admin.site.register(Subcategorie)
admin.site.register(TypeProduct)