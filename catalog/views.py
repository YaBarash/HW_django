from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from catalog.services import get_categories_from_cache
from version.forms import VersionForm
from version.models import Version


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.user = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['version_form'] = VersionForm()
        return context

    #     VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
    #     if self.request.method == 'POST':
    #         context['formset'] = VersionFormset(self.request.POST, instance=self.object)
    #     else:
    #         context['formset'] = VersionFormset(instance=self.object)
    #     return context
    #
    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     formset = context['formset']
    #     if formset.is_valid() and form.is_valid():
    #         self.object = form.save()
    #         formset.instance = self.object
    #         formset.save()
    #         return super().form_valid(form)
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return ProductForm
        if user.has_perm("catalog.set_published") and user.has_perm("catalog.change_description") and user.has_perm("catalog.change_category"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()
        for product in products:
            active_versions = Version.objects.filter(id=product.pk, is_active=True).last()
            if active_versions:
                product.active = active_versions.version_name
            else:
                product.active = 'Отсутствует'

        context['object_list'] = products
        return context


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f'{name} ({phone}): {message}')
        return render(request, 'catalog/contacts.html')

class CategoryListView(ListView):
    model = Category
    template_name = "catalog/categories_list.html"

    def get_queryset(self):
        return get_categories_from_cache()
