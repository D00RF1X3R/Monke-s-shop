from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class RangeValidator(object):
    def __init__(self, min_value, max_value):
        if min_value >= max_value:
            raise RuntimeError(f'{min_value} должно быть меньше, чем {max_value}')
        self.min_value, self.max_value = min_value, max_value
        self.validators = [MinValueValidator(min_value), MaxValueValidator(max_value)]

    def __call__(self, value):
        try:
            [validator(value) for validator in self.validators]
        except ValidationError:
            raise ValidationError(f'{value} должен лежать в диапазоне от {self.min_value} до {self.max_value}')