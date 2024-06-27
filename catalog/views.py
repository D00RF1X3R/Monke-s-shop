from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q, Min, Max, Count
from catalog.models import Product, ProductImage
from business.models import Seller, SellerData
from core.models import Universe, Category
from users.models import Rating, Cart, CustomerData
from django.template.loader import render_to_string
from django.views.generic import TemplateView, View


class ProductListView(TemplateView):
    template_name = 'catalog\catalog.html'
    def post(self, request):
        product = get_object_or_404(Product, id=request.POST.get("id"))
        customer_data = get_object_or_404(CustomerData, user=request.user)
        action_type = request.POST.get("type")
        if action_type == 'favorite':
            if product in customer_data.favorite_products.all():
                customer_data.favorite_products.remove(product)
            else:
                customer_data.favorite_products.add(product)
        elif action_type == 'to_cart':
            Cart.objects.get_or_create(
                customer=customer_data.user,
                product=product,
                count=1,
            )
        data = render_to_string("catalog/catalog.html", {"product": product, "customer": customer_data, "type": action_type})
        return JsonResponse({"data": data})
        
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
        min_max_price = Product.objects.aggregate(Min("price"), Max("price"))
        context["min_max_price"] = min_max_price
        products = products.filter(price__gte=min_max_price["price__min"])
        products = products.filter(price__lte=min_max_price["price__max"]).order_by("-price")
        return context
    def get_popular_products(self):
        context = self.get_context_data()
        context["products"] = Product.objects.annotate(num_marks=Count('marks')).order_by('-num_marks')
    def get_nonpopular_products(self):
        context = self.get_context_data()
        context["products"] = Product.objects.annotate(num_marks=Count('marks')).order_by('num_marks')

class ProductDetailView(TemplateView):
    template_name = 'product\product.html'
    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        customer_data = get_object_or_404(CustomerData, user=request.user)
        Cart.objects.get_or_create(
            customer=customer_data.user,
            product=product,
            count = 1,
        )
        data = render_to_string("product/product.html", {"product": product, "customer": customer_data})
        return JsonResponse({"data": data})
    def get_context_data(self, id):
        context = super().get_context_data()
        product = get_object_or_404(Product.objects.filter(id=id))
        product_marks = Rating.objects.filter(product=id).values_list('mark', flat=True)
        if product_marks:
            marks_count = len(product_marks)
            product_rating = sum(product_marks)/marks_count
        else:
            product_rating = 0
            marks_count = 0
        context["product"] = product
        context["images"] = ProductImage.objects.filter(product=id)
        context["product_rating"] = product_rating
        context["marks_count"] = marks_count
        context["is_verified"] = get_object_or_404(SellerData.objects.filter(user=product.seller)).is_verified
        return context

class filter_product(View):
    def post(self, request):
        product = get_object_or_404(Product, id=request.POST.get("id"))
        customer_data = get_object_or_404(CustomerData, user=request.user)
        Cart.objects.get_or_create(
            customer=customer_data.user,
            product=product,
            count=1,
        )
        data = render_to_string("catalog/async/catalog.html", {"product": product, "customer": customer_data})
        return JsonResponse({"data": data})

    def get(self, request):
        universes = request.GET.getlist("universe[]")
        categories = request.GET.getlist("category[]")
        sellers = request.GET.getlist("seller[]")
        min_price = request.GET["min_price"]
        max_price = request.GET["max_price"]
        search_query = request.GET.get('q')

        products = Product.objects.all()

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
        products = products.filter(price__lte=max_price).order_by("price")


        data = render_to_string("catalog/async/catalog.html", {"products": products})
        return JsonResponse({"data": data})

