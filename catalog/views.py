from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from catalog.models import Product, ProductImage
from business.models import SellerData, Seller
from core.models import Universe, Category
from django.template.loader import render_to_string

def ProductListView(request, category_id=None, universe_id=None):
    template = 'catalog\product_list.html'
    category = None
    universe = None
    categories = None
    universes = None
    seller = None
    sellers = None
    categories = Category.objects.all()
    universes = Universe.objects.all()
    sellers = Seller.objects.all()
    products = Product.objects.all()
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category_id=category_id)
    if universe_id:
        universe = get_object_or_404(Universe, id=universe_id)
        products = products.filter(universe_id=universe_id)

    return render(request, template, {
            'category': category,
            'categories': categories,
            'universe': universe,
            'universes': universes,
            'products': products,
            'sellers': sellers
            })


def ProductDetailView(request, id, universe_id=None, category_id=None):
    template = 'catalog\product_detail.html'
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(request, template, context)

def filter_product(request):
    universes = request.GET.getlist("universe[]")
    categories = request.GET.getlist("category[]")
    sellers = request.GET.getlist("seller[]")

    products = Product.objects.all().order_by("-id")

    if len(universes) > 0:
        products = products.filter(universe__id__in=universes).distinct()
    if len(categories) > 0:
        products = products.filter(category__id__in=categories).distinct()
    if len(sellers) > 0:
        products = products.filter(seller__id__in=sellers).distinct()

    data = render_to_string("catalog/async/product_list.html", {"products": products})
    return JsonResponse({"data": data})
