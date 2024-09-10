from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogUpdateView, BlogListView, BlogDetailView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('list/', BlogListView.as_view(), name='blog_list'),
    path('view/<slug:the_slug_blog>/', BlogDetailView.as_view(), name='blog_view'),
    path('update/<slug:the_slug_blog>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<slug:the_slug_blog>/', BlogDeleteView.as_view(), name='blog_delete'),
]