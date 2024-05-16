### Library Management System Documentation

Modules:

1. **book.py**: This module contains the `Book` class, which represents a book in the library. It provides methods for creating, validating, and manipulating book objects.

The BookManager class manages a collection of books and interacts with storage to save and load book data.

In the __init__ method, the storage parameter is used to initialize the storage for the book data.

The add_book method adds a new book to the collection. It takes various parameters for book details and creates a new Book object with them. If any of the provided parameters are invalid, it raises a ValueError.

The list_books method prints details of all the books in the collection.

The _save_books method converts the book objects into dictionaries and saves them to the storage.

The load_books method loads the book data from the storage and initializes the collection with it.


2. **checkout.py**: This module contains the `CheckoutManager` class, which manages the checkout process for books in the library. It allows users to check out and return books.


The CheckoutManager class manages a list of checkouts and interacts with storage to save and load checkout data.

In the __init__ method, the storage parameter is used to initialize the storage for checkout data, and the book_manager parameter is used to interact with book data.

The checkout_book method allows a user to checkout a book. It first checks if the book exists and is available for checkout. Then, it creates a new Checkout object, updates the book quantity, saves the checkout data, and prints status messages.

The return_book method allows a user to return a checked-out book. It searches for the book in the list of checkouts, marks it as returned, updates the book quantity, saves the checkout data, and prints status messages.

The _save_checkouts method saves the list of checkouts to the storage, and the load_checkouts method loads the list of checkouts from the storage.

3. **library.py**: In the new structure, I have added a `library.py` module, which serves as the central module responsible for orchestrating the interactions between different components of the library management system. This newly added module serves as the core of the library management system. This module contains the `Library` class, which acts as the central hub for managing books, users, and checkouts in the library. It provides methods for adding books, listing books, adding users, and checking out books.

The Library class manages the overall functionality of the library system.
In the __init__ method, instances of BookManager, UserManager, and CheckoutManager are created to manage books, users, and checkouts respectively. Data is loaded from storage into these managers.

The add_book, list_books, add_user, and checkout_book methods delegate their respective tasks to the appropriate manager classes (BookManager, UserManager, CheckoutManager). These methods encapsulate the functionality of adding books, listing books, adding users, and checking out books within the library system.


4. **main.py**: This module contains the main program logic for interacting with the library management system. It provides a command-line interface for users to perform various actions such as adding books, listing books, adding users, and checking out books.

The main_menu function displays the main menu options for the Library Management System and returns the user's choice.

The main function is the main entry point of the program. It creates an instance of the Library class and enters a loop to interact with the user.

Based on the user's choice from the main menu, corresponding methods of the Library class are called to perform operations such as adding a book, listing books, adding a user, checking out a book, or exiting the program.

5. **models.py**: This module contains the data models used in the library management system, including the `Book`, `User`, and `Checkout` classes.

The Book class represents a book entity with various attributes such as title, author, ISBN, etc. It includes validation methods for ensuring the correctness of attribute values.

The User class represents a user entity with a unique user ID assigned automatically upon creation.

The Checkout class represents a checkout transaction, indicating which user has checked out which book. It includes a method to mark the book as returned.

Each class includes docstrings explaining the purpose and usage of the class and its methods.
Validation methods are provided within the Book class to ensure that attributes meet certain criteria (e.g., valid ISBN format).

The to_dict and from_dict methods are implemented in both Book and User classes to facilitate serialization and deserialization of objects to/from dictionaries.

6. **storage.py**: This module contains the `JSONStorage` class, which provides functionality for saving and loading data to and from JSON files.

The JSONStorage class provides functionality for saving and loading data to/from a JSON file.
Upon initialization, it takes the filename as input, specifying the file to read from or write to.

The save_data method accepts a Python list or dictionary containing the data to be saved. It opens the file in write mode and uses the json.dump method to write the data in JSON format with an indentation of 4 spaces.

The load_data method reads data from the JSON file. It attempts to open the file in read mode and uses the json.load method to load the data from the file into a Python list or dictionary. If the file is not found (e.g., during the initial load or if the file has been deleted), it returns None.

7. **user.py**: This module contains `UserManager` class.

The UserManager class is responsible for managing user data, including adding new users, saving user data, and loading user data from storage.

Upon initialization, it takes a storage object as input, which is an instance of JSONStorage class responsible for handling JSON file operations.

The add_user method adds a new user to the user list using the provided name. It then saves the updated user data to the storage.

The _save_users method is a private method responsible for converting user objects to dictionary format using the to_dict method defined in the User class and saving the user data to the storage using the save_data method of the storage object.

The load_users method loads user data from the storage using the load_data method of the storage object. If data is found, it populates the users list with User objects created from the loaded data using the from_dict method defined in the User class.


### How to Use:

1. **Adding Books**:
   - Use the `add_book` method in the `Library` class by providing the necessary details such as title, author, ISBN, publication, genre, shelf number, and quantity.
   - Example:
     
     library.add_book("Harry Potter", "J.K. Rowling", "9780545582889", "Scholastic", "Fantasy", "A1", 5)


2. **Listing Books**:
   - Use the `list_books` method in the `Library` class to display a list of all books in the library.
   - Example:
     library.list_books()


3. **Adding Users**:
   - Use the `add_user` method in the `Library` class to add a new user to the library.
   - Example:
     
     library.add_user("John Doe")


4. **Checking Out Books**:
   - Use the `checkout_book` method in the `Library` class to check out a book for a user by providing the user ID and ISBN of the book.
   - Example:
     
     library.checkout_book("12345", "9780545582889")


5. **Running the Program**:
   - Execute the `main.py` script to start the library management system.
   - Use the command : python </path/to/directory/>main.py
   - Follow the prompts in the command-line interface to perform various actions such as adding books, listing books, adding users, and checking out books.



