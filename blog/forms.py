from blog.models import Blog
from catalog.forms import StyleFormMixin
from django import forms


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"


class BlogModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "preview", "content", "published", "views")
