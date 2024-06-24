from django.views.generic import TemplateView
from catalog.views import ProductListView, filter_product
from django.http import JsonResponse
from django.template.loader import render_to_string

class HomeView(ProductListView):
    template_name = "homepage/home.html"

    


    
