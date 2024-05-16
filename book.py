import re
from models import Book

class BookManager:
    def __init__(self, storage):
        """
        Initialize the BookManager with the provided storage.

        Args:
            storage: An instance of a storage class (e.g., JSONStorage).
        """
        self.storage = storage
        self.books = []

    def add_book(self, title, author, isbn, publication, genre, shelf_number, quantity):
        """
        Add a new book to the collection.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            publication (str): The publication of the book.
            genre (str): The genre of the book.
            shelf_number (str): The shelf number of the book.
            quantity (int): The quantity of the book available.

        Raises:
            ValueError: If any of the provided parameters are invalid.
        """
        # Create a new Book object
        book = Book(title, author, isbn, publication, genre, shelf_number, quantity)
        # Add the book to the collection
        self.books.append(book)
        # Save the updated collection to the storage
        self._save_books()

    def list_books(self):
        """List all the books in the collection."""
        for book in self.books:
            print(book)

    def _save_books(self):
        """Save the collection of books to the storage."""
        data = [book.to_dict() for book in self.books]
        self.storage.save_data(data)

    def load_books(self):
        """Load the collection of books from the storage."""
        data = self.storage.load_data()
        if data:
            self.books = [Book.from_dict(item) for item in data]
