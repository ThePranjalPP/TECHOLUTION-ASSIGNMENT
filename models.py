import re

class Book:
    def __init__(self, title, author, isbn, publication, genre, shelf_number, quantity):
        """
        Initializes a Book object with the provided attributes.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN (International Standard Book Number) of the book.
            publication (str): The publication name of the book.
            genre (str): The genre of the book.
            shelf_number (str): The shelf number where the book is stored.
            quantity (int): The quantity of copies of the book available.

        Raises:
            ValueError: If any of the input parameters fail validation.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication = publication
        self.genre = genre
        self.shelf_number = shelf_number
        self.quantity = quantity

        # Validate input parameters
        if not self._validate_isbn():
            raise ValueError("Invalid ISBN")
        if not self._validate_author():
            raise ValueError("Invalid author name")
        if not self._validate_publication():
            raise ValueError("Invalid publication name")
        if not self._validate_genre():
            raise ValueError("Invalid genre")
        if not self._validate_shelf_number():
            raise ValueError("Invalid shelf number")
        if not self._validate_quantity():
            raise ValueError("Invalid quantity")

    def _validate_isbn(self):
        """
        Validates the ISBN format (10 or 13 characters).

        Returns:
            bool: True if the ISBN is valid, False otherwise.
        """
        isbn_pattern = r"^\d{10}$|^\d{13}$"
        return bool(re.match(isbn_pattern, self.isbn))

    def _validate_author(self):
        """
        Validates the author name format.

        Returns:
            bool: True if the author name is valid, False otherwise.
        """
        author_pattern = r"^[A-Za-z .]+$"
        return bool(re.match(author_pattern, self.author))

    def _validate_publication(self):
        """
        Validates the publication name format.

        Returns:
            bool: True if the publication name is valid, False otherwise.
        """
        publication_pattern = r"^[A-Za-z .]+$"
        return bool(re.match(publication_pattern, self.publication))

    def _validate_genre(self):
        """
        Validates the genre format.

        Returns:
            bool: True if the genre is valid, False otherwise.
        """
        genre_pattern = r"^[A-Za-z ]+$"
        return bool(re.match(genre_pattern, self.genre))

    def _validate_shelf_number(self):
        """
        Validates the shelf number format.

        Returns:
            bool: True if the shelf number is valid, False otherwise.
        """
        shelf_pattern = r"^[a-zA-Z0-9-]+$"
        return bool(re.match(shelf_pattern, self.shelf_number))

    def _validate_quantity(self):
        """
        Validates the quantity format.

        Returns:
            bool: True if the quantity is valid, False otherwise.
        """
        try:
            quantity = int(self.quantity)
            return quantity >= 0
        except ValueError:
            return False

    def __str__(self):
        """
        Returns a string representation of the Book object.

        Returns:
            str: A string containing the book's attributes.
        """
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Publication: {self.publication}, Genre: {self.genre}, Shelf Number: {self.shelf_number}, Quantity: {self.quantity}"

    def to_dict(self):
        """
        Converts the Book object to a dictionary.

        Returns:
            dict: A dictionary containing the book's attributes.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "publication": self.publication,
            "genre": self.genre,
            "shelf_number": self.shelf_number,
            "quantity": self.quantity
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Book object from a dictionary.

        Args:
            data (dict): A dictionary containing the book's attributes.

        Returns:
            Book: A Book object initialized with the provided attributes.
        """
        return cls(data["title"], data["author"], data["isbn"], data["publication"], data["genre"], data["shelf_number"], data["quantity"])

class User:
    last_user_number = 0  # Class attribute to keep track of the last assigned user number

    def __init__(self, name):
        """
        Initializes a User object with the provided name and assigns a unique user ID.

        Args:
            name (str): The name of the user.

        Returns:
            None
        """
        self.name = name
        User.last_user_number += 1  # Increment the last assigned user number
        self.user_id = f"LIB_USER_{User.last_user_number}"  # Assign the new user ID

    def to_dict(self):
        """
        Converts the User object to a dictionary.

        Returns:
            dict: A dictionary containing the user's attributes.
        """
        return {
            "name": self.name,
            "user_id": self.user_id
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a User object from a dictionary.

        Args:
            data (dict): A dictionary containing the user's attributes.

        Returns:
            User: A User object initialized with the provided attributes.
        """
        return cls(data["name"], data["user_id"])

class Checkout:
    def __init__(self, user_id, isbn, returned=False):
        """
        Initializes a Checkout object with the provided user ID and ISBN.

        Args:
            user_id (str): The ID of the user who is checking out the book.
            isbn (str): The ISBN of the book being checked out.
            returned (bool): Whether the book has been returned (default is False).

        Returns:
            None
        """
        if not isinstance(user_id, str):
            raise ValueError("User ID must be a string")
        if not isinstance(isbn, str):
            raise ValueError("ISBN must be a string")
        if len(isbn) not in (10, 13):
            raise ValueError("ISBN must be either 10 or 13 characters long")

        self.user_id = user_id
        self.isbn = isbn
        self.returned = returned

    def mark_returned(self):
        """
        Marks the book as returned.

        Returns:
            None
        """
        self.returned = True

    def to_dict(self):
        """
        Converts the Checkout object to a dictionary.

        Returns:
            dict: A dictionary containing the checkout's attributes.
        """
        return {
            "user_id": self.user_id,
            "isbn": self.isbn,
            "returned": self.returned
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Checkout object from a dictionary.

        Args:
            data (dict): A dictionary containing the checkout's attributes.

        Returns:
            Checkout: A Checkout object initialized with the provided attributes.
        """
        return cls(data["user_id"], data["isbn"], data["returned"])
