from django.contrib import admin

from order.models import Payment, OrderStatus, ProductInOrder, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

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

class OrderStatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderStatus._meta.fields]

    class Meta:
        model = OrderStatus

admin.site.register(OrderStatus, OrderStatusAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Payment._meta.fields]

    class Meta:
        model = Payment

admin.site.register(Payment, PaymentAdmin)