from django.urls import path
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # List all books
    path("books/", list_books, name="list_books"),

    # Library detail view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # User registration
    path("register/", register, name="register"),

    # User login
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),

    # User logout
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
