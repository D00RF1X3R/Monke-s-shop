from django import forms


class UserMultiChoiceWidget(forms.widgets.CheckboxSelectMultiple):
    template_name = 'widgets/multiple_select.html'
