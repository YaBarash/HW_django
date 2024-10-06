from catalog.forms import StyleFormMixin
from django import forms

from clients.models import Client


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"