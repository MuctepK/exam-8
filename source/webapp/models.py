from django.db import models
from django.contrib.auth.models import User
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

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(verbose_name='Текст отзыва', max_length=512)
    mark = models.DecimalField(verbose_name='Оценка', max_digits=3, decimal_places=2)

    def __str__(self):
        return "Оценка {} к продукту {}".format(self.author, self.product)