from django import forms

from core.models import Category, Universe
from users.models import Customer, CustomerData


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [Customer.username.field.name, Customer.email.field.name]


class CustomerCreateForm(forms.ModelForm):
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(),
    )

    password_repeat = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(),
    )

    favorite_categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label='Любимые категории'
    )

    favorite_universes = forms.ModelMultipleChoiceField(
        queryset=Universe.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label='Любимые вселенные'
    )

    class Meta:
        model = Customer
        fields = [Customer.username.field.name, Customer.email.field.name]

    def __init__(self, *args, **kwargs):
        super(CustomerCreateForm, self).__init__(*args, **kwargs)
        self.fields[Customer.email.field.name].required = True

    def clean(self):
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
