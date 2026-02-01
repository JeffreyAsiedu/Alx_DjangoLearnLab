# Retrieve Operation

**Goal:** Retrieve and display all attributes of the book just created.

**Python Command:**

```python
# Get the book (assuming it is the only one or filtering by title)
book = Book.objects.get(title="1984")

# Display attributes
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Year: {book.publication_year}")


```

**Output:** # Details: 1984, George Orwell, 1949
