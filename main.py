from library import Library

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Checkout Book")
    print("5. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    library = Library()
    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)
            print("Book added.")
        elif choice == '2':
            library.list_books()
        elif choice == '3':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            library.add_user(name, user_id)
            print("User added.")
        elif choice == '4':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            library.checkout_book(user_id, isbn)
            print("Book checked out.")
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
