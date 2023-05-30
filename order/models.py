from django.contrib.auth.models import User
from shop.models import Product
from django.db import models


class Order(models.Model):

    STATUS_CART = 1
    STATUS_WAITING_FOR_PAYMENT = 2
    STATUS_PAID = 3

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None,
                             verbose_name='Покупатель')
    status = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, blank=True, null=True, default=None,
                               verbose_name='Статус')
    total_amount = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True, default=0,
                                 verbose_name='Сумма')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлён')
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True, default=None,
                                verbose_name='Платёж')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    session_key = models.CharField(max_length=100, blank=True, null=True, default=None,
                                   verbose_name='Ключ сессии')

    def __str__(self):
        user = self.user if self.user != None else f'Anonymus user with session key:{self.session_key}'
        return f'Заказ №{self.id} - {user} - Сумма: {self.total_amount}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class ProductInOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False, blank=False,
                                verbose_name='Товар')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True,
                              verbose_name='Заказ')
    price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True, default=None,
                                verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    total_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True, default=None,
                                      verbose_name='Сумма')

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.product.price
        self.total_price = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product}'

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None,
                             verbose_name='Покупатель')
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=0,
                                 verbose_name='Сумма')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    is_done = models.BooleanField(default=False, verbose_name='Завершена')

    def __str__(self):
        return f'{self.amount}'

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'

### СИГНАЛЫ ###

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=ProductInOrder)
@receiver(post_delete, sender=ProductInOrder)
def update_order_total(sender, instance, **kwargs):
    try:
        order = instance.order
        total = order.productinorder_set.aggregate(total=models.Sum('total_price')).get('total', 0) or 0
        order.total_amount = total
        order.save()
    except Order.DoesNotExist:
        pass

