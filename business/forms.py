from django import forms
from django.core.validators import MinValueValidator
from django.forms import widgets
from django.shortcuts import get_object_or_404

from business.models import Seller, SellerData
from catalog.models import Product


class SellerCreateForm(forms.ModelForm):
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(),
    )

    password_repeat = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = Seller
        fields = [Seller.username.field.name, Seller.email.field.name]

    def __init__(self, *args, **kwargs):
        super(SellerCreateForm, self).__init__(*args, **kwargs)
        self.fields[Seller.email.field.name].required = True

    def clean(self, commit=True):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if password != password_repeat:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self):
        seller = Seller.objects.create_user(
            username=self.cleaned_data[Seller.username.field.name],
            password=self.cleaned_data['password'],
            email=self.cleaned_data[Seller.email.field.name],
        )

        SellerData.objects.create(user=seller,)


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [Product.name.field.name,
                  Product.description.field.name,
                  Product.category.field.name,
                  Product.universe.field.name,
                  Product.price.field.name,
                  Product.preview.field.name,]
        widgets = {
            Product.price.field.name: widgets.NumberInput(attrs={'min': 1}),
        }

    def save(self, user_id):
        Product.objects.create(
            seller=get_object_or_404(Seller, id=user_id),
            name=self.cleaned_data[Product.name.field.name],
            description=self.cleaned_data[Product.description.field.name],
            category=self.cleaned_data[Product.category.field.name],
            universe=self.cleaned_data[Product.universe.field.name],
            price=self.cleaned_data[Product.price.field.name],
            preview=self.cleaned_data[Product.preview.field.name],
        )
