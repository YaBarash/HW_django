from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, TemplateView

from clients.forms import ClientForm, EmailSettingsForm, MailingMessageForm
from clients.models import Client, EmailSettings, MailLog, MailingMessage, MailingClient


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

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Client.objects.all()
        else:
            return Client.objects.filter(owner=self.request.user)


class ClientsUpdateView(UserPassesTestMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:client_list')

    def test_func(self):
        return self.request.user == self.get_object().owner or self.request.user.is_superuser or self.request.user.is_staff


class ClientsDeleteView(PermissionRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients:client_list')
    permission_required = 'clients.delete_client'


class EmailSettingsCreateView(PermissionRequiredMixin, CreateView):
    model = EmailSettings
    form_class = EmailSettingsForm
    success_url = reverse_lazy('clients:emailsettings_list')
    permission_required = 'clients.add_emailsettings'


class EmailSettingsListView(PermissionRequiredMixin, ListView):
    model = EmailSettings
    permission_required = 'clients.view_emailsettings'


class EmailSettingsDeleteView(PermissionRequiredMixin, DeleteView):
    model = EmailSettings
    success_url = reverse_lazy('clients:emailsettings_list')
    permission_required = 'clients.delete_emailsettings'


class EmailSettingsUpdateView(PermissionRequiredMixin, UpdateView):
    model = EmailSettings
    form_class = EmailSettingsForm
    success_url = reverse_lazy('clients:emailsettings_list')
    permission_required = 'clients.change_emailsettings'


class MailingMessageCreateView(PermissionRequiredMixin, CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('clients:mailingmessage_list')
    permission_required = 'clients.add_mailingmessage'


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


class MailLogListView(PermissionRequiredMixin, ListView):
    model = MailLog
    permission_required = 'clients.change_maillog'

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_admin:
            return MailLog.objects.all()
        else:
            return MailLog.objects.filter(owner=self.request.user)


class MailingClientListView(ListView):
    model = MailingClient


def toggle_client(request, pk, client_pk):
    if MailingClient.objects.filter(
            client_id=client_pk,
            mailing_id=pk
    ).exists():
        MailingClient.objects.filter(
            client_id=client_pk,
            mailing_id=pk
        ).delete()
    else:
        MailingClient.objects.create(
            client_id=client_pk,
            mailing_id=pk
        )

    return redirect(reverse('clients:mailingclient_list', args=[pk]))
