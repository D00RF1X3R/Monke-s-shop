from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, UpdateView

from core.models import Universe
from users.forms import CustomerCreateForm, CustomerProfileForm, CustomerImageForm, CustomerFavoriteCategoriesForm, \
    CustomerFavoriteUniversesForm, CustomerBalanceAddForm
from users.models import Customer, CustomerData, BalanceAddHistory


class SignupView(FormView):
    form_class = CustomerCreateForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, View):
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


class CartView(LoginRequiredMixin, View):
    pass


class FavoritesView(LoginRequiredMixin, View):
    pass


class FavoriteCategoriesView(LoginRequiredMixin, View):
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


class FavoriteUniversesView(LoginRequiredMixin, View):
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


class BalanceAddView(LoginRequiredMixin, FormView):
    form_class = CustomerBalanceAddForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/balance/add.html'

    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)


class BalanceHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        template = 'users/balance/history.html'
        histories = BalanceAddHistory.objects.filter(customer=request.user)
        context = {'histories': histories}
        return render(request, template, context)


class CartHistoryView(LoginRequiredMixin, View):
    pass
