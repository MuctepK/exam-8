from django.db import models
CATEGORY_CHOICES = [
    ('other', 'Другое'),
    ('kitchen', 'Кухня'),
    ('electronics', 'Электроника'),
    ('children', 'Дети')
]


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    category = models.CharField(verbose_name='Категория', max_length=64, choices=CATEGORY_CHOICES,
                                default=CATEGORY_CHOICES[0][0])
    description = models.TextField(null=True, blank=True, verbose_name='Описание', max_length=512)
    img = models.ImageField(verbose_name='Картинка', null=True, blank=True, upload_to='product_pics')
