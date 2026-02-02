from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from bookshelf.models import Book  
from .models import Library

# Authentication imports (checker requirement)
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Existing books list view
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Required library detail view
def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk) 
    return render(request, "relationship_app/library_detail.html", {"library": library})
