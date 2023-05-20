from django.contrib import admin
from django.utils.html import format_html

from .models import Payment, OrderStatus, ProductInOrder, Order

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0
    readonly_fields = ['display_product_image']

    def display_product_image(self, obj):
        product = obj.product
        if product.productimage_set.exists():
            image = product.productimage_set.first()
            return format_html('<img src="{}" width="25%" height="25%" />', image.photo.url)
        return '-'

    display_product_image.short_description = 'Product Image'  # Заголовок столбца

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]
    
    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

class OrderStatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderStatus._meta.fields]

    class Meta:
        model = OrderStatus

admin.site.register(OrderStatus, OrderStatusAdmin)

class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Payment._meta.fields]

    class Meta:
        model = Payment

admin.site.register(Payment, PaymentAdmin)