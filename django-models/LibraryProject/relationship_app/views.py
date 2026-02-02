from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from bookshelf.models import Book
from .models import Library

# Authentication imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Library detail view
def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, "relationship_app/library_detail.html", {"library": library})

# User registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
