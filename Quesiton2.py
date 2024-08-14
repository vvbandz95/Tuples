# 2 

def add_book(library, book):
    """
    Add a new book to the library if it does not already exist.
    
    Args:
    library (list of tuples): Existing list of books, where each book is a tuple (title, author).
    book (tuple): The new book to add, where the book is a tuple (title, author).
    
    Returns:
    str: Message indicating whether the book was added or already exists.
    """
    if book in library:
        return "The book already exists in the library."
    else:
        library.append(book)
        return "The book has been added to the library."

# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Example usage
new_book1 = ("To Kill a Mockingbird", "Harper Lee")
new_book2 = ("1984", "George Orwell")  # Duplicate book

# Adding new books
print(add_book(library, new_book1))  # Expected output: The book has been added to the library.
print(add_book(library, new_book2))  # Expected output: The book already exists in the library.

# Print the updated library
print("\nUpdated Library:")
for book in library:
    print(f"Title: {book[0]}, Author: {book[1]}")
