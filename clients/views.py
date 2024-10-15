import random

from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, TemplateView

from blog.models import Blog
from clients.forms import ClientForm, EmailSettingsForm, MailingMessageForm
from clients.models import Client, EmailSettings, MailLog, MailingMessage, MailingClient


class HomePageView(TemplateView):
    template_name = 'clients/home_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        all_email = EmailSettings.objects.all().count()
        is_on_email = EmailSettings.objects.filter(status__in=['Создана', 'Запущена']).count()
        unique_clients = Client.objects.values('email').distinct().count()
        blogs = Blog.objects.order_by('slug')[:3]
        context = {'all_email': all_email, 'is_on_email': is_on_email, 'unique_clients': unique_clients, 'blogs':blogs}
        return context



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
    permission_required = 'clients.delete_emailsettings'


class EmailSettingsUpdateView(UpdateView):
    model = EmailSettings
    form_class = EmailSettingsForm
    success_url = reverse_lazy('clients:emailsettings_list')

    @staticmethod
    def edit_activate(request, pk):
        mailing_item = get_object_or_404(EmailSettings, pk=pk)
        if mailing_item.status == EmailSettings.STATUS_CREATED or mailing_item.status == EmailSettings.STATUS_STARTED:
            mailing_item.status = EmailSettings.STATUS_DONE
        else:
            mailing_item.status = EmailSettings.STATUS_STARTED
        mailing_item.save()
        return redirect('clients:emailsettings_list')


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
