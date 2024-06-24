from django.core.exceptions import PermissionDenied


class SellerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.type == 'Продавец':
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
