from django.urls import path
from .views import list_books, LibraryDetailView 
urlpatterns = [
    # List all books
    path("books/", list_books, name="list_books"),

    # Library detail view using class-based view
    path(
        "library/<int:pk>/", 
        LibraryDetailView.as_view(), 
        name="library_detail"
    ),
]
