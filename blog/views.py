from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.models import Blog


# class BlogListView(ListView):
#     model = Blog
# class BlogDetailView(DetailView):

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'published']
    success_url = reverse_lazy('catalog:product_list')
# class BlogUpdateView(UpdateView):
#
# class BlogDeleteView(DeleteView):
