from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_admin', 'price', 'created', 'updated', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['created', 'updated', 'available']

    def image_admin(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='70' />")
        return "None"

    image_admin.__name__ = 'Картинка'




# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)


