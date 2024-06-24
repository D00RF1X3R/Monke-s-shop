from django.urls import path
from business.views import SignupView, ProfileView, ProductsListView, ProductChangeView, ProductAddView

app_name = 'business'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/add/', ProductAddView.as_view(), name='product_add'),
    path('products/change/<int:pk>', ProductChangeView.as_view(), name='product_change'),
]
