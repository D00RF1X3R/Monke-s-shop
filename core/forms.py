from django import forms

from core.models import User


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(
            attrs={
                'minlength': 1,
                'maxlength': User._meta.get_field('username').max_length,
            }
        ),
    )

    class Meta:
        model = User
        fields = [User.email.field.name]


class UserImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [User.image.field.name]