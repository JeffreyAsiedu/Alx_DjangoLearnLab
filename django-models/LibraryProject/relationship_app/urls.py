from django.urls import path
from . import views  # import the module
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # List all books
    path("books/", views.list_books, name="list_books"),

    # Library detail view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # User registration (checker requires views.register)
    path("register/", views.register, name="register"),

    # User login
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),

    # User logout
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
