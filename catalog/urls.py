from django.urls import include, path
from catalog.views import ProductListView, ProductDetailView, filter_product

app_name = "catalog"
urlpatterns = [
    path("", ProductListView, name="products"),
    path("filter-products/", filter_product, name="filter-products"),
    path("<int:id>", ProductDetailView, name="product_detail"),
]
