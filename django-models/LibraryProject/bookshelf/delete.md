# Delete Operation

**Goal:** Delete the book created and confirm the deletion by trying to retrieve all books.

**Python Command:**

```python
from bookshelf.models import Book


# 1. Fetch the object (using the NEW title)
book = Book.objects.get(title="Nineteen Eighty-Four")

# 2. Delete it
book.delete()

# 3. Confirm deletion by checking all books
all_books = Book.objects.all()
print(all_books)

```

**Output:** # <QuerySet []>
