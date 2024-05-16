from models import Checkout

class CheckoutManager:
    def __init__(self, storage, book_manager):
        """
        Initialize the CheckoutManager with the provided storage and book manager.

        Args:
            storage: An instance of a storage class (e.g., JSONStorage) for storing checkout data.
            book_manager: An instance of the BookManager class for managing book data.
        """
        self.storage = storage
        self.book_manager = book_manager
        self.checkouts = []

    def checkout_book(self, user_id, isbn):
        """
        Checkout a book for a user.

        Args:
            user_id (str): The ID of the user checking out the book.
            isbn (str): The ISBN of the book to be checked out.

        Prints:
            Status messages indicating whether the checkout was successful or not.
        """
        # Check if the book exists in the library
        book = self.book_manager.get_book_by_isbn(isbn)
        if not book:
            print("Book not found.")
            return

        # Check if the book is available for checkout
        if book.quantity <= 0:
            print("Book not available for checkout.")
            return

        # Create a new Checkout object and add it to the list of checkouts
        checkout = Checkout(user_id, isbn)
        self.checkouts.append(checkout)
        
        # Update the quantity of the book in the library
        self.book_manager.update_book_quantity(isbn, book.quantity - 1)
        
        # Save the updated list of checkouts
        self._save_checkouts()
        print("Book checked out.")

    def return_book(self, user_id, isbn):
        """
        Return a checked-out book.

        Args:
            user_id (str): The ID of the user returning the book.
            isbn (str): The ISBN of the book to be returned.

        Prints:
            Status messages indicating whether the return was successful or not.
        """
        # Search for the book in the list of checkouts for the user
        for checkout in self.checkouts:
            if checkout.user_id == user_id and checkout.isbn == isbn:
                # Mark the book as returned
                checkout.mark_returned()
                # Update the quantity of the book in the library
                self.book_manager.update_book_quantity(isbn, self.book_manager.get_book_by_isbn(isbn).quantity + 1)
                # Save the updated list of checkouts
                self._save_checkouts()
                print("Book returned successfully.")
                return

        print("Book not found in user's checkout list.")

    def _save_checkouts(self):
        """Save the list of checkouts to the storage."""
        data = [checkout.to_dict() for checkout in self.checkouts]
        self.storage.save_data(data)

    def load_checkouts(self):
        """Load the list of checkouts from the storage."""
        data = self.storage.load_data()
        if data:
            self.checkouts = [Checkout.from_dict(item) for item in data]
