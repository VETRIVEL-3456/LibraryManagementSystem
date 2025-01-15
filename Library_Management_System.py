
import os

class Library:
    def __init__(self):
        self.books = []
        self.issued_books = {}

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added successfully!")

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Book '{book_name}' removed successfully!")
        else:
            print(f"Book '{book_name}' not found.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(f" - {book}")

    def issue_book(self, book_name, user_name):
        if book_name in self.books and book_name not in self.issued_books:
            self.issued_books[book_name] = user_name
            print(f"Book '{book_name}' issued to {user_name}.")
        elif book_name in self.issued_books:
            print(f"Book '{book_name}' is already issued to {self.issued_books[book_name]}.")
        else:
            print(f"Book '{book_name}' not available.")

    def return_book(self, book_name):
        if book_name in self.issued_books:
            del self.issued_books[book_name]
            print(f"Book '{book_name}' returned successfully!")
        else:
            print(f"Book '{book_name}' was not issued.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_name = input("Enter the name of the book to add: ")
            library.add_book(book_name)
        elif choice == "2":
            book_name = input("Enter the name of the book to remove: ")
            library.remove_book(book_name)
        elif choice == "3":
            library.display_books()
        elif choice == "4":
            book_name = input("Enter the name of the book to issue: ")
            user_name = input("Enter the name of the user: ")
            library.issue_book(book_name, user_name)
        elif choice == "5":
            book_name = input("Enter the name of the book to return: ")
            library.return_book(book_name)
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
