from django.contrib import admin
from application.models import ProductList

class PruductListaAdmin (admin.ModelAdmin):
    list_display = ('brand_name', 'model_name', 'date_entry')
    list_filter = ('date_entry',)


admin.site.register(ProductList, PruductListaAdmin)
