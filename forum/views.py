from django.db.models import Sum, Value, IntegerField
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView

from catalog.models import Product
from core.models import Category, Universe
from users.models import Rating


class ForumsView(ListView):
    model = Category

    def get_template_names(self):
        return 'forum/forums.html'


class SubForumsView(ListView):
    model = Universe

    def get_template_names(self):
        return 'forum/sub_forums.html'

    def get_context_data(self, **kwargs):
        context = super(SubForumsView, self).get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, id=self.kwargs['category_id'])
        return context


class ChatsView(TemplateView):
    template_name = 'forum/chats.html'

    def get_context_data(self, **kwargs):
        context = super(ChatsView, self).get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, id=self.kwargs['category_id'])
        context['universe'] = get_object_or_404(Universe, id=self.kwargs['universe_id'])

        context['products'] = Product.objects.filter(universe=context['universe'], category=context['category'])
        context['products'] = context['products'].annotate(
            chat_rating=Sum('rating', output_field=IntegerField())
        )
        context['products'] = context['products'].order_by('-chat_rating')

        for product in context['products']:
            product_ratings = Rating.objects.filter(product=product)
            if len(product_ratings) == 0:
                product.chat_rating = 0
            else:
                mark_sum = product_ratings.aggregate(Sum('mark'))['mark__sum']
                product.chat_rating = mark_sum - len(product_ratings) * 3
        return context


class FloodView(View):
    pass


class ProductDiscussionView(View):
    pass
