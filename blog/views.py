from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.forms import BlogModeratorForm, BlogForm
from blog.models import Blog


class BlogCreateView(PermissionRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')
    permission_required = 'blog.add_blog'

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     object_publ = Blog.objects.filter(published=True)
    #     context['object_publ'] = object_publ
    #     return context

    def get_queryset(self):
        if self.request.user.is_staff:  # если контент-менеджер
            return Blog.objects.all()  # выводим все блоги
        else:
            return Blog.objects.filter(published=True)  # только опубликованные


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'published', ]
    permission_required = 'blog.change_blog'

    def get_success_url(self):
        return reverse_lazy('blog:blog_view', kwargs={'pk': self.object.id})

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return BlogForm
        if user.has_perm('blog.add_blog') and user.has_perm("blog.change_blog") and user.has_perm("blog.delete_blog"):
            return BlogModeratorForm
        raise PermissionDenied


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    permission_required = 'blog.delete_blog'
