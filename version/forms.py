from django.forms import ModelForm
from django.urls import reverse_lazy

from catalog.forms import StyleFormMixin
from version.models import Version


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
        success_url = reverse_lazy("catalog:product_list")