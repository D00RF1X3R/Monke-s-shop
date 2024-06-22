from django.core.exceptions import PermissionDenied


class CustomerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.type == 'Покупатель':
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied