from book import BookManager
from user import UserManager
from checkout import CheckoutManager
from storage import JSONStorage

class Library:
    def __init__(self):
        """
        Initialize the Library with book, user, and checkout managers.

        This constructor creates instances of BookManager, UserManager, and CheckoutManager
        to manage books, users, and checkouts respectively. It also loads data from storage
        into these managers.

        Args:
            None

        Returns:
            None
        """
        # Create instances of BookManager, UserManager, and CheckoutManager
        self.book_manager = BookManager(JSONStorage("books.json"))
        self.user_manager = UserManager(JSONStorage("users.json"))
        self.checkout_manager = CheckoutManager(JSONStorage("checkouts.json"), self.book_manager)

        # Load data from storage into the managers
        self.book_manager.load_books()
        self.user_manager.load_users()
        self.checkout_manager.load_checkouts()

    def add_book(self, title, author, isbn, publication, genre, shelf_number, quantity):
        """
        Add a new book to the library.

        This method delegates the task of adding a new book to the BookManager.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            publication (str): The publication of the book.
            genre (str): The genre of the book.
            shelf_number (str): The shelf number of the book.
            quantity (int): The quantity of the book.

        Returns:
            None
        """
        self.book_manager.add_book(title, author, isbn, publication, genre, shelf_number, quantity)

    def list_books(self):
        """
        List all the books in the library.

        This method delegates the task of listing all the books to the BookManager.

        Args:
            None

        Returns:
            None
        """
        self.book_manager.list_books()

    def add_user(self, name):
        """
        Add a new user to the library.

        This method delegates the task of adding a new user to the UserManager.

        Args:
            name (str): The name of the user.

        Returns:
            None
        """
        self.user_manager.add_user(name)

    def checkout_book(self, user_id, isbn):
        """
        Checkout a book for a user.

        This method delegates the task of checking out a book to the CheckoutManager.

        Args:
            user_id (str): The ID of the user checking out the book.
            isbn (str): The ISBN of the book to be checked out.

        Returns:
            None
        """
        self.checkout_manager.checkout_book(user_id, isbn)
