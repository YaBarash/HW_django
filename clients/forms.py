from catalog.forms import StyleFormMixin
from django import forms

from clients.models import Client, EmailSettings, MailingMessage


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

class EmailSettingsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = EmailSettings
        fields = "__all__"

class MailingMessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingMessage
        fields = "__all__"