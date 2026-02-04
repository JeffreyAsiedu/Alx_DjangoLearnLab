from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from bookshelf.models import Book
from .models import Library
from django.contrib.auth.decorators import user_passes_test

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

# Login view
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'


# Logout view
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})


def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
