from django.shortcuts import render
from bookshelf.models import Book  # Import Book from bookshelf app

def list_books(request):
    # Query all books
    books = Book.objects.all()
    
    # Render the required template
    return render(request, "relationship_app/list_books.html", {"books": books})
