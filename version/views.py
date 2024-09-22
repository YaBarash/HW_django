from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from version.forms import Version, VersionForm


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm


class VersionListView(ListView):
    model = Version


# class VersionDetailView(DetailView):
#     model = Version
#
#
# class VersionUpdateView(UpdateView):
#     model = Version
#     fields = "__all__"
#
#
# class VersionDeleteView(DeleteView):
#     model = Version
