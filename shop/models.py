from django.db import models
from django.urls import reverse
from main.utils import make_slug


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Наименование')
    code = models.CharField(max_length=255, unique=True, verbose_name='Код')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена')
    description = models.TextField(blank=True, verbose_name='Описание')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True,
                                 verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Слаг')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлён')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = make_slug(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'slug': self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                blank=True, null=True, default=None,
                                verbose_name='Товар')
    photo = models.ImageField(upload_to='product_images/', verbose_name='Изображение')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлён')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'
