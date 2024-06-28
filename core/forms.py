from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

from core.models import User


class UserProfileForm(forms.Form):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(
            attrs={
                'minlength': 1,
                'maxlength': 20,
                'class': 'profile_card_user_info__name',
                'onchange': 'document.getElementById("change_profile_form").submit()'
            }
        ),
    )

    email = forms.EmailField(
        label='Почта',
        widget=forms.EmailInput(
            attrs={
                'minlength': 1,
                'maxlength': 40,
                'class': 'profile_card_user_info__e-mail',
                'onchange': 'document.getElementById("change_profile_form").submit()'
            }
        )
    )


class UserImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [User.image.field.name]


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))


class UserResetPasswordForm(PasswordResetForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Адрес эл. почты'}))


class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Новый пароль'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите новый пароль'}))


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Старый пароль'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Новый пароль'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите новый пароль'}))
