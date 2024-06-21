from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from users.forms import CustomerCreateForm, CustomerForm
from users.models import Customer, CustomerData


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

        main_form = CustomerForm(initial={
            Customer.email.field.name: customer.email,
            Customer.username.field.name: customer.username,
        },)

        context = {'form': main_form}
        return render(request, template, context)


class CartView(View):
    pass


class FavoritesView(View):
    pass


class BalanceAddView(View):
    pass


class HistoryView(View):
    pass
