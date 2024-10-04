from django import forms

from catalog.models import Product


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():

            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.DateTimeInput):
                field.widget.attrs['class'] = 'form-control flatpickr-basic'
            elif isinstance(field.widget, forms.DateInput):
                field.widget.attrs['class'] = 'form-control datepicker'
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs['class'] = 'form-control flatpickr-time'
            elif isinstance(field.widget, forms.widgets.SelectMultiple):
                field.widget.attrs['class'] = 'form-control select2 select2-multiple'
            elif isinstance(field.widget, forms.widgets.Select):
                field.widget.attrs['class'] = 'form-control select2'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    # def clean_name(self):
    #     prohibited_names = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
    #                         'радар']
    #     cleaned_data = self.cleaned_data.get('name')
    #     for i in prohibited_names:
    #         if i in cleaned_data.lower():
    #             raise forms.ValidationError('Ошибка! Недопустимое название товара!')
    #     return cleaned_data

    def clean(self):
        prohibited_names = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        cleaned_data = super().clean()
        cleaned_name = cleaned_data.get('name')
        cleaned_description = cleaned_data.get('description')
        for i in prohibited_names:
            if i == cleaned_name.lower() and i == cleaned_description.lower():
                raise forms.ValidationError('Ошибка! Недопустимое название и описание товара!')
            elif i == cleaned_description.lower():
                raise forms.ValidationError('Ошибка! Недопустимое описание товара!')
            elif i == cleaned_name.lower():
                raise forms.ValidationError('Ошибка! Недопустимое название товара!')
