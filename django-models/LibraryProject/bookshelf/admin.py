from django.contrib import admin
from .models import Book


# Define a custom Admin class to customize the view
class BookAdmin(admin.ModelAdmin):
    # 1. Display specific fields in the list view
    list_display = ("title", "author", "publication_year")

    # 2. Add filters to the right sidebar
    list_filter = ("publication_year", "author")

    # 3. Add a search box at the top
    search_fields = ("title", "author")


# Register the model with the custom admin class
admin.site.register(Book, BookAdmin)
