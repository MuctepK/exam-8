from django.urls import path

from webapp.views import ProductCreateView
from .views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(),name='index'),
    path('products/create', ProductCreateView.as_view(), name='create_product')
]

app_name = 'webapp'
