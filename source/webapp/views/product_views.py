from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/index.html'


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
