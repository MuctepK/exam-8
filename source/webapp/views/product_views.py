from django.contrib.auth.mixins import PermissionRequiredMixin
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


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/detail.html'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create.html'
    permission_required = 'webapp.add_product'
    permission_denied_message = 'Доступ запрещен'

    def get_success_url(self):
        return reverse('webapp:detail_product', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/update.html'
    permission_required = 'webapp.change_product'
    permission_denied_message = 'Доступ запрещен'

    def get_success_url(self):
        return reverse('webapp:detail_product', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin,DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'
    permission_denied_message = 'Доступ запрещен'
