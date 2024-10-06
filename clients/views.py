from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from clients.forms import ClientForm
from clients.models import Client, EmailSettings, MailLog, MailingMessage


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
