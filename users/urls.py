from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse, reverse_lazy

from users.views import ProfileView, SignupView, CartView, FavoritesView, BalanceAddView, HistoryView

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path(
        'password_change/',
        PasswordChangeView.as_view(template_name='users/password_change/start.html'),
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
                                  email_template_name='users/password_reset/email.html'),
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
                                         success_url=reverse_lazy('users:password_reset_complete')),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(template_name='users/password_reset/complete.html'),
        name='password_reset_complete',
    ),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('favorites/', FavoritesView.as_view(), name='favorites'),
    path('cart/', CartView.as_view(), name='cart'),
    path('balance_add/', BalanceAddView.as_view(), name='balance_add'),
    path('history/', HistoryView.as_view(), name='history'),
]
