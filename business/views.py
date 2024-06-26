from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, UpdateView
from business.forms import SellerCreateForm, ProductAddForm
from business.mixins import SellerRequiredMixin
from business.models import SellerData, Seller
from catalog.models import Product
from core.forms import UserProfileForm, UserImageForm


class SignupView(FormView):
    form_class = SellerCreateForm
    template_name = 'business/signup.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileView(SellerRequiredMixin, View):
    def get(self, request):
        template = 'business/profile.html'

        seller = request.user
        seller_data = get_object_or_404(SellerData, user=seller.id)
        form = UserProfileForm(initial={
            Seller.email.field.name: seller.email,
            Seller.username.field.name: seller.username,
        })
        form.fields[Seller.email.field.name].label = 'Контактная почта'
        form.fields[Seller.username.field.name].label = 'Имя продавца'

        image_form = UserImageForm()

        context = {
            'form': form,
            'form_image': image_form,
            'seller_data': seller_data
        }

        return render(request, template, context)

    def post(self, request):
        customer = request.user
        form = UserProfileForm(request.POST)
        form_image = UserImageForm(request.POST, request.FILES, instance=customer)

        if form.is_valid():
            customer.username = form.cleaned_data['username']
            customer.email = form.cleaned_data[Seller.email.field.name]
            customer.save()

        if form_image.is_valid():
            form_image.save()

        return redirect("business:profile")


class ProductsListView(SellerRequiredMixin, View):

    def get(self, request):
        template_name = 'business/products.html'
        products = Product.objects.filter(seller=request.user)
        context = {
            'products': products
        }

        return render(request, template_name, context)

    @staticmethod
    def post(request):
        print(request.POST)
        product_id = request.POST.get('id')
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return JsonResponse({})


class ProductAddView(SellerRequiredMixin, FormView):
    template_name = 'business/product_add.html'
    form_class = ProductAddForm
    success_url = reverse_lazy('business:products')

    def form_valid(self, form):
        form.save(self.request.user.id)
        return super().form_valid(form)


class ProductChangeView(UpdateView):
    model = Product
    fields = [
        Product.name.field.name,
        Product.description.field.name,
        Product.category.field.name,
        Product.universe.field.name,
        Product.price.field.name,
        Product.preview.field.name
    ]
    template_name = 'business/product_change.html'
    success_url = reverse_lazy('business:products')

    def get_context_data(self, **kwargs):
        context = super(ProductChangeView, self).get_context_data(**kwargs)
        context['product_id'] = self.kwargs.get('pk')
        return context
