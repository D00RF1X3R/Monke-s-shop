from django.db.models import Sum, F, Value, Subquery, OuterRef
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from catalog.models import Product
from users.forms import CustomerCreateForm, CustomerProfileForm, CustomerImageForm, CustomerFavoriteCategoriesForm, \
    CustomerFavoriteUniversesForm, CustomerBalanceAddForm
from users.mixins import CustomerRequiredMixin
from users.models import Customer, CustomerData, BalanceAddHistory, Cart, BuyHistory, Rating


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def is_rated(product):
    subquery = Rating.objects.filter(product=product).exists()
    return subquery


class SignupView(FormView):
    form_class = CustomerCreateForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileView(CustomerRequiredMixin, View):
    def get(self, request):
        template = 'users/profile.html'

        customer = request.user
        customer_data = get_object_or_404(CustomerData, user=customer.id)
        form = CustomerProfileForm(initial={
            Customer.email.field.name: customer.email,
            Customer.username.field.name: customer.username,
        })
        image_form = CustomerImageForm()

        context = {
            'form': form,
            'form_image': image_form,
            'customer_data': customer_data
        }

        return render(request, template, context)

    def post(self, request):
        customer = request.user
        form = CustomerProfileForm(request.POST)
        form_image = CustomerImageForm(request.POST, request.FILES, instance=customer)

        if form.is_valid():
            customer.username = form.cleaned_data['username']
            customer.email = form.cleaned_data[Customer.email.field.name]
            customer.save()

        if form_image.is_valid():
            form_image.save()

        return redirect("users:profile")


class CartView(CustomerRequiredMixin, View):
    def get(self, request, **kwargs):
        template = 'users/cart.html'
        customer_data = get_object_or_404(CustomerData, user=request.user.id)
        cart_products = Cart.objects.filter(customer=request.user.id)
        sum_price = cart_products.aggregate(total=Sum(F('count') * F('product__price')))['total']

        context = {
            'cart_products': cart_products,
            'sum_price': sum_price,
            'balance': customer_data.balance
        }
        return render(request, template, context)

    def post(self, request):
        if not is_ajax(request):
            cart_products = Cart.objects.filter(customer=request.user.id)
            sum_price = cart_products.aggregate(total=Sum(F('count') * F('product__price')))['total']

            for cart_product in cart_products:
                BuyHistory.objects.create(
                    customer=request.user,
                    product=cart_product.product,
                    count=cart_product.count
                )
            cart_products.delete()

            customer_data = get_object_or_404(CustomerData, user=request.user.id)
            customer_data.balance -= sum_price
            customer_data.save()

            return redirect('users:cart')
        else:
            cart_product = get_object_or_404(Cart, id=request.POST.get('id'))
            json = {}

            if request.POST.get('action') in ('add', 'subtract'):
                coef = 1
                if request.POST.get('action') == 'subtract':
                    coef = -1
                cart_product.count += coef
                cart_product.save()
                json['new_count'] = cart_product.count
            elif request.POST.get('action') == 'delete':
                cart_product.delete()
            elif request.POST.get('action') == 'favorite':
                customer_data = get_object_or_404(CustomerData, user=request.user)
                if cart_product.product in customer_data.favorite_products.all():
                    customer_data.favorite_products.remove(cart_product.product)
                else:
                    customer_data.favorite_products.add(cart_product.product)

            cart_products = Cart.objects.filter(customer=request.user.id)
            sum_price = cart_products.aggregate(total=Sum(F('count') * F('product__price')))['total']
            json['new_sum_price'] = sum_price
            return JsonResponse(json)


class FavoriteProductsView(CustomerRequiredMixin, View):
    def get(self, request, **kwargs):
        template = 'users/favorite_products.html'
        customer_data = get_object_or_404(CustomerData, user=request.user)

        context = {'favorite_products': customer_data.favorite_products.all()}
        return render(request, template, context)

    @staticmethod
    def post(request):
        customer_data = get_object_or_404(CustomerData, user=request.user)
        product = get_object_or_404(Product, id=request.POST.get('id'))
        if product in customer_data.favorite_products.all():
            customer_data.favorite_products.remove(product)
        else:
            customer_data.favorite_products.add(product)

        response = {}

        return JsonResponse(response)


class FavoriteCategoriesView(CustomerRequiredMixin, View):
    def get(self, request):
        template = 'users/favorite_categories.html'

        customer_data = get_object_or_404(CustomerData, user=request.user.id)
        form = CustomerFavoriteCategoriesForm(initial={
            'favorite_categories': customer_data.favorite_categories.all()
        })
        context = {'form': form}
        return render(request, template, context)

    def post(self, request):
        form = CustomerFavoriteCategoriesForm(request.POST)
        if form.is_valid():
            customer_data = get_object_or_404(CustomerData, user=request.user.id)
            customer_data.favorite_categories.clear()
            for category in form.cleaned_data['favorite_categories']:
                customer_data.favorite_categories.add(category)
            customer_data.save()

        return redirect('users:favorite_categories')


class FavoriteUniversesView(CustomerRequiredMixin, View):
    def get(self, request):
        template = 'users/favorite_universes.html'

        customer_data = get_object_or_404(CustomerData, user=request.user.id)
        form = CustomerFavoriteUniversesForm(initial={
            'favorite_universes': customer_data.favorite_universes.all()
        })
        context = {'form': form}
        return render(request, template, context)

    def post(self, request):
        form = CustomerFavoriteUniversesForm(request.POST)
        if form.is_valid():
            customer_data = get_object_or_404(CustomerData, user=request.user.id)
            customer_data.favorite_universes.clear()
            for universe in form.cleaned_data['favorite_universes']:
                customer_data.favorite_universes.add(universe)
            customer_data.save()

        return redirect('users:favorite_universes')


class BalanceAddView(CustomerRequiredMixin, FormView):
    form_class = CustomerBalanceAddForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/balance/add.html'

    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)


class BalanceHistoryView(CustomerRequiredMixin, View):
    def get(self, request):
        template = 'users/balance/history.html'
        histories = BalanceAddHistory.objects.filter(customer=request.user)
        context = {'histories': histories}
        return render(request, template, context)


class CartHistoryView(CustomerRequiredMixin, View):
    def get(self, request):
        template = 'users/buy_history.html'
        context = {
            'buy_histories': {}
        }

        buy_histories = BuyHistory.objects.filter(customer=request.user)
        for buy_history in buy_histories:
            rating = Rating.objects.filter(user=request.user, product=buy_history.product).first()
            if rating:
                buy_history.product_rating = rating.mark
            else:
                buy_history.product_rating = 0

            if buy_history.date in context['buy_histories']:
                context['buy_histories'][buy_history.date].append(buy_history)
            else:
                context['buy_histories'][buy_history.date] = [buy_history]

        return render(request, template, context)

    @staticmethod
    def post(request):
        product = get_object_or_404(Product, id=request.POST.get('product'))
        Rating.objects.create(
            user=request.user,
            product=product,
            mark=request.POST.get('mark')
        )
        return JsonResponse({'product': product.id, 'mark': request.POST.get('mark')})
