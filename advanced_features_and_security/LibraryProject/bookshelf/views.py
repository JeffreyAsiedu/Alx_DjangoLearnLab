from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import ExampleForm 


@login_required
@permission_required("bookshelf.view_book", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})
