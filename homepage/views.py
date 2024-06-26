from catalog.views import ProductListView

class HomeView(ProductListView):
    template_name = "homepage/geekShop.html"

