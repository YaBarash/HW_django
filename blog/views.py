from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'published']
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    slug_url_kwarg = 'the_slug_blog'


class BlogDetailView(DetailView):
    model = Blog
    slug_url_kwarg = 'the_slug_blog'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'published']
    success_url = reverse_lazy('blog:blog_list')
    slug_url_kwarg = 'the_slug_blog'


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    slug_url_kwarg = 'the_slug_blog'
