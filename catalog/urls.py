from django.urls import include, path
from catalog.views import ProductListView, ProductDetailView, filter_product

app_name = "catalog"
urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path("filter-products/", filter_product.as_view(), name="filter-products"),
    path("<int:id>", ProductDetailView.as_view(), name="product_detail"),
]