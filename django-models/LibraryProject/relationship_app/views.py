from django.shortcuts import render
from bookshelf.models import Book  
from .models import Library

def list_books(request):
    # Query all books
    books = Book.objects.all()
    
    # Render the required template
    return render(request, "relationship_app/list_books.html", {"books": books})
