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

    def get_average(self):
        reviews = self.reviews.all()
        if reviews:
            total = sum([review.mark for review in reviews])
            return round(total/len(reviews), 2)
        return 0

    def get_star(self):
        average = self.get_average()
        number = []
        for i in range(1, 6):
            if average > 0.00:
                if average - 1 < 0.00:
                    number.append(str(average * 100))
                    average -= 1
                else:
                    average -= 1
                    number.append(str(100))
            else:
                number.append(str(0))
        return number



class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(verbose_name='Текст отзыва', max_length=512)
    mark = models.DecimalField(verbose_name='Оценка', max_digits=3, decimal_places=2)

    def __str__(self):
        return "Оценка {} к продукту {}".format(self.author, self.product)


    def get_star(self):
        mark = self.mark
        number = []
        for i in range(1, 6):
            if mark > 0.00:
                if mark - 1 < 0.00:
                    number.append(str(mark * 100))
                    mark -= 1
                else:
                    mark -= 1
                    number.append(str(100))
            else:
                number.append(str(0))
        return number