from django.db import models

# Author model represents a writer who can have multiple books.
class Author(models.Model):
    # Stores the author's full name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model represents a book written by an author.
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=200)

    # Year the book was published
    publication_year = models.IntegerField()

    # Foreign key establishing a one-to-many relationship:
    # One Author -> Many Books
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title