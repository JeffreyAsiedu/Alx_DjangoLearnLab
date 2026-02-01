# Create Operation

**Goal:** Create a Book instance with the title "1984", author "George Orwell", and publication year 1949.

**Python Command:**

```python
from bookshelf.models import Book

# Create the instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)


```

**Output**

# <Book: 1984 by George Orwell>
