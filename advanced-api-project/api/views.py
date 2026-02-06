from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework

# Allows anyone (authenticated or not) to view all books
class BookListView(generics.ListAPIView):
    """
    ListAPIView for retrieving all Book instances.

    Features:
    - Filtering by title, publication_year, and author
    - Searching by title and author name
    - Ordering by title and publication_year

    Access:
    - Public (no authentication required)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtering options
    filterset_fields = ['title', 'publication_year', 'author']

    # Search options
    search_fields = ['title', 'author__name']

    # Ordering options
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']
    
# Allows anyone to retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    RetrieveAPIView for fetching a single Book by its ID.
    Read-only access is allowed for all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Only authenticated users can create new books
class BookCreateView(generics.CreateAPIView):
    """
    CreateAPIView for adding a new Book.
    Only authenticated users are permitted to create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Only authenticated users can update books
class BookUpdateView(generics.UpdateAPIView):
    """
    UpdateAPIView for modifying an existing Book.
    Only authenticated users are permitted to update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Only authenticated users can delete books
class BookDeleteView(generics.DestroyAPIView):
    """
    DestroyAPIView for deleting a Book instance.
    Only authenticated users are permitted to delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
