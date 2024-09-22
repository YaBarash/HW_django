from django.forms import ModelForm

from catalog.forms import StyleFormMixin
from version.models import Version


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"