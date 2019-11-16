from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from webapp.forms import ProductForm
from webapp.models import Product
from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        products = self.get_queryset()
        context['average_of'] = self.get_average_of_products(products.all())
        print(context['average_of'])
        return context

    def get_average_of_products(self, products):
        average_of = {}
        for product in products:
            average_of[product.pk] = self.get_average(product.reviews.all())
        return average_of

    def get_average(self,reviews):
        if reviews:
            total = sum([review.mark for review in reviews])
            return round(total/len(reviews), 2)
        return 0

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        reviews = self.object.reviews.all()
        context['reviews'] = reviews
        context['average'] = self.get_average(reviews)
        return context

    def get_average(self,reviews):
        if reviews:
            total = sum([review.mark for review in reviews])
            return round(total/len(reviews),2)
        return 0

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create.html'

    def get_success_url(self):
        return reverse('webapp:detail_product', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/update.html'

    def get_success_url(self):
        return reverse('webapp:detail_product', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('webapp:index')
