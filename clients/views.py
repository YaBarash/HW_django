from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, TemplateView

from clients.forms import ClientForm, EmailSettingsForm, MailingMessageForm
from clients.models import Client, EmailSettings, MailLog, MailingMessage

class HomePageView(TemplateView):
    template_name = 'clients/home_page.html'

class ClientsCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientsDetailView(DetailView):
    model = Client
    success_url = reverse_lazy('clients:client_list')


class ClientsListView(ListView):
    model = Client


class ClientsUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:client_list')


class ClientsDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:client_list')


class EmailSettingsCreateView(CreateView):
    model = EmailSettings
    form_class = EmailSettingsForm
    success_url = reverse_lazy('clients:emailsettings_list')

class EmailSettingsListView(ListView):
    model = EmailSettings

class EmailSettingsDeleteView(DeleteView):
    model = EmailSettings
    success_url = reverse_lazy('clients:emailsettings_list')

class EmailSettingsUpdateView(UpdateView):
    model = EmailSettings
    form_class = EmailSettingsForm
    success_url = reverse_lazy('clients:emailsettings_list')

class MailingMessageCreateView(CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('clients:mailingmessage_list')

class MailingMessageUpdateView(UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('clients:mailingmessage_list')

class MailingMessageListView(ListView):
    model = MailingMessage
    success_url = reverse_lazy('clients:mailingmessage_list')

class MailingMessageDeleteView(DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('clients:mailingmessage_list')