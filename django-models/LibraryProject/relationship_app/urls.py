from django.urls import path
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book


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

    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),

    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book')
]

