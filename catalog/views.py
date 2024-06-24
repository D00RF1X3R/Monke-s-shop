from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from catalog.models import Product
from business.models import Seller
from core.models import Universe, Category
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

        return context


class ProductDetailView(TemplateView):
    template_name = 'catalog\product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product = get_object_or_404(Product.objects.filter(id=kwargs.get("id")))
        context["product"] = product
        

        return context

class filter_product(View):
    def get(self, request):
        universes = request.GET.getlist("universe[]")
        categories = request.GET.getlist("category[]")
        sellers = request.GET.getlist("seller[]")
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

        data = render_to_string("catalog/async/product_list.html", {"products": products})
        return JsonResponse({"data": data})