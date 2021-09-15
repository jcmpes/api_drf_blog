""" Post admin classes. """

# Django
from django.contrib import admin

# Models
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """User admin."""

    list_display = (
        'pk',
        'title',
        'user',
        'published'
    )

    search_fields = (
        'title',
        'user',
    )

    list_filter = (
        'published',
        'date',
    )
