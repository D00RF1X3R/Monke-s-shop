from django.urls import path, reverse_lazy
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)

from core.forms import UserAuthenticationForm, UserResetPasswordForm, UserSetPasswordForm, UserPasswordChangeForm
from users.views import (ProfileView,
                         SignupView,
                         CartView,
                         CartHistoryView,
                         FavoriteProductsView,
                         FavoriteCategoriesView,
                         FavoriteUniversesView,
                         BalanceAddView,
                         BalanceHistoryView)

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html',
                                     authentication_form=UserAuthenticationForm),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/password_change/start.html',
            success_url=reverse_lazy('users:password_change_done'),
            form_class=UserPasswordChangeForm
        ),
        name='password_change_start',
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(template_name='users/password_change/done.html'),
        name='password_change_done',
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(template_name='users/password_reset/start.html',
                                  success_url=reverse_lazy('users:password_reset_done'),
                                  email_template_name='users/password_reset/email.html',
                                  form_class=UserResetPasswordForm),
        name='password_reset_start'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(template_name='users/password_reset/done.html'),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='users/password_reset/confirm.html',
                                         success_url=reverse_lazy('users:password_reset_complete'),
                                         form_class=UserSetPasswordForm),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(template_name='users/password_reset/complete.html'),
        name='password_reset_complete',
    ),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('favorites/', FavoriteProductsView.as_view(), name='favorites'),
    path('favorite_categories/', FavoriteCategoriesView.as_view(), name='favorite_categories'),
    path('favorite_universes/', FavoriteUniversesView.as_view(), name='favorite_universes'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart_history/', CartHistoryView.as_view(), name='cart_history'),
    path('balance_add/', BalanceAddView.as_view(), name='balance_add'),
    path('balance_history/', BalanceHistoryView.as_view(), name='balance_history'),
]
