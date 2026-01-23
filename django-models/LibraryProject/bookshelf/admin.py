from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Filters to appear in the sidebar
    list_filter = ('author', 'publication_year')

    # Searchable fields
    search_fields = ('title', 'author')

# Register the model with the custom admin
admin.site.register(Book, BookAdmin)
