import re
from datetime import date

from django.core.exceptions import ValidationError
from django.forms import (
    CharField, DateField, IntegerField, ModelForm
)

from viewer.models import Category, Product


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')




class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = '__all__'

    title = CharField(validators=[capitalized_validator])
    quantity = IntegerField(min_value=1, max_value=99)
    released = PastMonthField()

    def clean_description(self):
        # Force each sentence of the description to be capitalized.
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result['quantity'] > 10:
            raise ValidationError(
                "Please contact our staff to double check the stock availability."
            )
        return result
