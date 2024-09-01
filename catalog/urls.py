from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', contacts, name='contacts'),
]
