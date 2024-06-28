from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, BooleanField, Count, F, OuterRef, Subquery, Exists, Value, Avg, FloatField
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import TemplateView, ListView

from catalog.models import Product
from core.models import Category, Universe
from forum.models import FloodMessage, ProductMessage
from users.models import BuyHistory, Rating, Cart, CustomerData


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
            chat_rating=Avg('marks__mark'),
            message_count=Count('productmessage', distinct=True)
        )
        context['products'] = context['products'].order_by('-chat_rating')
        context['flood_count'] = FloodMessage.objects.filter(
            category=self.kwargs['category_id'],
            universe=self.kwargs['universe_id']
        ).count()
        return context


class FloodView(LoginRequiredMixin, TemplateView):
    template_name = 'forum/flood.html'

    def get_context_data(self, **kwargs):
        context = super(FloodView, self).get_context_data(**kwargs)
        context['messages'] = FloodMessage.objects.filter(category=self.kwargs['category_id'],
                                                          universe=self.kwargs['universe_id'])
        context['category'] = get_object_or_404(Category, id=self.kwargs['category_id'])
        context['universe'] = get_object_or_404(Universe, id=self.kwargs['universe_id'])
        return context


class ProductDiscussionView(LoginRequiredMixin, View):

    def get(self, request, product_id):
        template_name = 'forum/product_discussion.html'
        context = {}
        product = get_object_or_404(Product, id=product_id)

        buy_history = BuyHistory.objects.filter(customer=OuterRef('customer'), product=product)
        is_upvoted = ProductMessage.objects.filter(id=OuterRef('id'), users_upvotes=request.user)
        is_downvoted = ProductMessage.objects.filter(id=OuterRef('id'), users_downvotes=request.user)

        context['messages'] = ProductMessage.objects.filter(product=product).annotate(
            customer=F('user'),
            is_buyed=Exists(Subquery(buy_history.values('customer')), output_field=BooleanField()),
            is_upvoted=Exists(Subquery(is_upvoted.values('id')), output_field=BooleanField()),
            is_downvoted=Exists(Subquery(is_downvoted.values('id')), output_field=BooleanField()),
            rating=Count('users_upvotes') - Count('users_downvotes'),
        )
        context['product'] = product
        context['is_buyed'] = BuyHistory.objects.filter(customer=request.user, product=product).exists()
        context['range'] = range(5)

        rating = Rating.objects.filter(user=request.user, product=product).first()
        if rating:
            context['product_rating'] = rating.mark
        else:
            context['product_rating'] = 0
        return render(request, template_name, context)

    @staticmethod
    def post(request, product_id):
        action = request.POST.get('action')
        product = get_object_or_404(Product, id=product_id)
        json = {}

        if action == 'upvote' or action == 'downvote':
            message = get_object_or_404(ProductMessage, id=request.POST.get('message_id'))
            json['new_count'] = int(request.POST.get('message_rating'))
            if action == 'upvote':
                if request.user in message.users_upvotes.all():
                    message.users_upvotes.remove(request.user)
                    json['new_count'] -= 1
                    json['upvote'] = False
                else:
                    message.users_upvotes.add(request.user)
                    json['new_count'] += 1
                    if request.user in message.users_downvotes.all():
                        message.users_downvotes.remove(request.user)
                        json['new_count'] += 1
                        json['downvote'] = False
                    json['upvote'] = True
            else:
                if request.user in message.users_downvotes.all():
                    message.users_downvotes.remove(request.user)
                    json['new_count'] += 1
                    json['downvote'] = False
                else:
                    message.users_downvotes.add(request.user)
                    json['new_count'] -= 1
                    if request.user in message.users_upvotes.all():
                        message.users_upvotes.remove(request.user)
                        json['new_count'] -= 1
                        json['upvote'] = False
                    json['downvote'] = True
        elif action == 'to_cart':
            customer_data = get_object_or_404(CustomerData, user=request.user)
            Cart.objects.get_or_create(
                customer=customer_data.user,
                product=product,
            )
        else:
            rating, _ = Rating.objects.update_or_create(
                user=request.user,
                product=product,
                create_defaults={'mark': 5}
            )
            rating.mark = request.POST.get('action')
            rating.save()
            json['mark'] = request.POST.get('action')

        return JsonResponse(json)
