from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = (
        "username",
        "email",
        "date_of_birth",
        "is_staff",
        "is_active",
    )

    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Information", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )


# Register CustomUser with CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

# Book Admin (existing)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("publication_year", "author")
    search_fields = ("title", "author")


admin.site.register(Book, BookAdmin)
