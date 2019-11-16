from django.urls import path

from webapp.views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView, ReviewCreateView, \
    ReviewUpdateView, ReviewDeleteView
from .views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('products/create/', ProductCreateView.as_view(), name='create_product'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
    path('reviews/<int:product_pk>/create/', ReviewCreateView.as_view(), name='create_review'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='update_review'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete_review')
]

app_name = 'webapp'
