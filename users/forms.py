from django import forms
from django.shortcuts import get_object_or_404

from core.models import Category, Universe
from users.models import Customer, CustomerData, BalanceAddHistory
from users.widgets import UserMultiChoiceWidget


class CustomerFavoriteCategoriesForm(forms.Form):
    favorite_categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=UserMultiChoiceWidget(),
        required=False,
        label=''
    )


class CustomerBalanceAddForm(forms.Form):
    amount = forms.IntegerField(min_value=1, max_value=100000, label='Сумма', initial=1)

    def save(self, current_user):
        amount = self.cleaned_data['amount']
        customer_data = get_object_or_404(CustomerData, user=current_user.id)

        balance_history = BalanceAddHistory.objects.create(
            customer=current_user,
            amount=amount
        )
        customer_data.balance += amount
        customer_data.save()
        balance_history.save()


class CustomerFavoriteUniversesForm(forms.Form):
    favorite_universes = forms.ModelMultipleChoiceField(
        queryset=Universe.objects.all(),
        widget=UserMultiChoiceWidget(),
        required=False,
        label=''
    )


class CustomerCreateForm(forms.ModelForm):
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
    )

    password_repeat = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}),
    )

    favorite_categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=UserMultiChoiceWidget(attrs={'label': 'Любимые категории'}),
        required=False,
        label='Любимые категории'
    )

    favorite_universes = forms.ModelMultipleChoiceField(
        queryset=Universe.objects.all(),
        widget=UserMultiChoiceWidget(attrs={'label': 'Любимые вселенные'}),
        required=False,
        label='Любимые вселенные'
    )

    class Meta:
        model = Customer
        fields = [Customer.username.field.name, Customer.email.field.name]
        widgets = {
            Customer.username.field.name: forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
            Customer.email.field.name: forms.EmailInput(attrs={'placeholder': 'Адрес эл. почты'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomerCreateForm, self).__init__(*args, **kwargs)
        self.fields[Customer.email.field.name].required = True

    def clean(self, commit=True):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if password != password_repeat:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self):
        customer = Customer.objects.create_user(
            username=self.cleaned_data[Customer.username.field.name],
            password=self.cleaned_data['password'],
            email=self.cleaned_data[Customer.email.field.name],
        )

        customer_data = CustomerData.objects.create(user=customer,)
        for category in self.cleaned_data['favorite_categories']:
            customer_data.favorite_categories.add(category)
        for universe in self.cleaned_data['favorite_universes']:
            customer_data.favorite_universes.add(universe)
