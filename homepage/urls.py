from django.urls import path
from homepage.views import HomeView
from catalog.views import filter_product

app_name = "homepage"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("filter-products/", filter_product.as_view(), name="filter-products"),

]
