from catalog.views import ProductListView
from users.models import CustomerData
from catalog.models import Product
from itertools import chain
from django.shortcuts import get_object_or_404

class HomeView(ProductListView):
    template_name = "homepage/geekShop.html"
    def get_context_data(self):
        context =  super().get_context_data()
        try:
            customer_data = CustomerData.objects.get(user=self.request.user.id)
        except CustomerData.DoesNotExist:
            customer_data = None
        if customer_data:
            favorite_categories = Product.objects.filter(category__id__in=customer_data.favorite_categories.all(),
                                                        universe__id__in=customer_data.favorite_universes.all())
            bad_products = Product.objects.exclude(category__id__in=customer_data.favorite_categories.all(),
                                                universe__id__in=customer_data.favorite_universes.all())
            favorite_products = list(chain(favorite_categories, bad_products))
            context["products"] = favorite_products
        return context




