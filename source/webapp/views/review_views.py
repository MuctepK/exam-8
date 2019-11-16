from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ReviewForm
from webapp.models import Review, Product


class ReviewCreateView(LoginRequiredMixin, CreateView):
    form_class = ReviewForm
    model = Review
    template_name = 'review/create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.product = self.get_product()
        return super().form_valid(form)

    def get_product(self):
        return Product.objects.get(id=self.kwargs['product_pk'])

    def get_success_url(self):
        return reverse('webapp:detail_product', kwargs={'pk':self.kwargs['product_pk']})


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/update.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.change_review'
    permission_denied_message = 'Доступ запрещен'

    def has_permission(self):
        return super().has_permission() or self.is_author(self.request.user)

    def is_author(self, user):
        return self.get_object().author == user


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    model = Review
    template_name = 'review/delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_review'
    permission_denied_message = 'Доступ запрещен'

    def has_permission(self):
        return super().has_permission() or self.is_author(self.request.user)

    def is_author(self, user):
        return self.get_object().author == user
