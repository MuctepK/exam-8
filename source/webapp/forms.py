from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['product', 'author']

    def clean_mark(self):
        mark = self.cleaned_data['mark']
        if not 5.00 >= mark >= 1.00:
            raise(ValidationError("Оценка может принимать значение от 1.00 до 5.00"))
        return mark
