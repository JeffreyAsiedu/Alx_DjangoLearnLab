from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer


# Public read-only list (optional)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Full CRUD — authenticated users only
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
