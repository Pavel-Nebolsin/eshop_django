from django.contrib import admin
from django.utils.html import format_html

from .models import Product, ProductImage, Category


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    readonly_fields = ['display_image']

    def display_image(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="25%" height="25%" />', obj.photo.url)
        return '-'

    display_image.short_description = 'Image'  # Заголовок столбца


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_active', 'display_images']

    def display_images(self, obj):
        images = obj.productimage_set.all()
        return format_html(
            ' '.join('<img src="{}" width="20%" height="20%" />'.format(image.photo.url) for image in images))

    display_images.short_description = 'Images'  # Заголовок столбца

    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'display_image','is_active']

    def display_image(self, obj):
        return format_html('<img src="{}" width="15%" height="15%" />', obj.photo.url)

    display_image.short_description = 'Image'  # Заголовок столбца

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)
