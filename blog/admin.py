from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at",)
    # list_filter = ("title",)
    search_fields = (
        "title",
        "content",
    )