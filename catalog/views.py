from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q, Min, Max
from catalog.models import Product
from business.models import Seller
from core.models import Universe, Category
from users.models import Rating
from django.template.loader import render_to_string
from django.views.generic import TemplateView, View


class ProductListView(TemplateView):
    template_name = 'catalog\product_list.html'
    def get_context_data(self):
        context = {}
        search_query = self.request.GET.get("q")
        
        products = Product.objects.all()
        context["products"] = products
        if search_query:
            q = None
            for word in search_query.split():
                q_aux = Q( name__icontains = word )
                q = ( q_aux & q ) if bool( q ) else q_aux
            context["products"] = products.filter(q)
            context["current_search"] = search_query

        context["categories"] = Category.objects.all()
        context["universes"] = Universe.objects.all()
        context["sellers"] = Seller.objects.all()
        context["min_max_price"] = Product.objects.aggregate(Min("price"), Max("price"))

        return context
    def get_popular_products(self):
        context = self.get_context_data()
        context["products"] = context["products"].filter()


class ProductDetailView(TemplateView):
    template_name = 'catalog\product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product = get_object_or_404(Product.objects.filter(id=kwargs.get("id")))
        product_marks = Rating.objects.filter(product=kwargs.get("id")).values_list('mark', flat=True)
        if product_marks:
            product_rating = sum(product_marks)/len(product_marks)
        else:
            product_rating = 0
        context["product"] = product
        context["product_rating"] = product_rating

        return context

class filter_product(View):
    def get(self, request):
        universes = request.GET.getlist("universe[]")
        categories = request.GET.getlist("category[]")
        sellers = request.GET.getlist("seller[]")
        min_price = request.GET["min_price"]
        max_price = request.GET["max_price"]
        search_query = request.GET.get('q')

        products = Product.objects.all().order_by("name")

        if len(universes) > 0:
            products = products.filter(universe__id__in=universes).distinct()
        if len(categories) > 0:
            products = products.filter(category__id__in=categories).distinct()
        if len(sellers) > 0:
            products = products.filter(seller__id__in=sellers).distinct()
        if search_query:
            q_aux = Q(name__icontains=search_query)
            products = products.filter(q_aux)
        
        products = products.filter(price__gte=min_price)
        products = products.filter(price__lte=max_price)

        data = render_to_string("catalog/async/product_list.html", {"products": products})
        return JsonResponse({"data": data})