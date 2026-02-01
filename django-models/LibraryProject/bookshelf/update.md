# Update Operation

**Goal:** Update the title of "1984" to "Nineteen Eighty-Four" and save the changes.

**Python Command:**

```python
# 1. Fetch the object
book = Book.objects.get(title="1984")

# 2. Modify the attribute
book.title = "Nineteen Eighty-Four"

# 3. Save to database
book.save()

# Verify the change
print(book.title)


```

**Output:** # Nineteen Eighty-Four
