# 1. import, from, as
import json  # Importing the json module to handle JSON file operations.
from datetime import datetime as dt  # Importing datetime and renaming it to 'dt' for easier use.

# 2. global variables
global_library_catalog = []  # Global variable to store the list of books.
global_member_list = []  # Global variable to store library members.
global_book_id = 0  # Global variable to keep track of book IDs.

# 3. class
class Book:
    """Represents a book in the library"""
    # 'class' keyword is used to define a class for creating book objects.
    
    def __init__(self, title, author):
        global global_book_id  # Using 'global' to modify the global variable `global_book_id`.
        global_book_id += 1  # Incrementing book ID.
        self.id = global_book_id  # Assigning a unique ID to the book.
        self.title = title  # Assigning book title.
        self.author = author  # Assigning book author.
        self.borrowed = False  # Default status of borrowed set to False.
        self.borrower = None  # No borrower assigned initially.

    def __str__(self):
        # Overriding the string representation of the Book object.
        status = "Available" if not self.borrowed else f"Borrowed by {self.borrower}"
        return f"[{self.id}] {self.title} by {self.author} - {status}"

# 4. def (defining functions)
def add_book(title, author):
    book = Book(title, author)  # Creating a new Book object.
    global_library_catalog.append(book)  # Adding the book to the library catalog.
    print(f"Book '{title}' added to the library.")

def list_books():
    if not global_library_catalog:  # 'not' keyword is used to check if the catalog is empty.
        print("No books in the library.")
    else:
        for book in global_library_catalog:  # 'for' loop to iterate through the list of books.
            print(book)

def borrow_book(member_name, book_id):
    for book in global_library_catalog:  # Iterating over books in the catalog.
        if book.id == book_id:  # Checking if the book ID matches.
            if book.borrowed:  # Checking if the book is already borrowed.
                print(f"Book '{book.title}' is already borrowed.")
                return
            book.borrowed = True  # Marking the book as borrowed.
            book.borrower = member_name  # Assigning the borrower.
            print(f"{member_name} borrowed '{book.title}'.")
            return
    print(f"No book found with ID: {book_id}")  # 'else' block to handle case where book isn't found.

def return_book(book_id):
    for book in global_library_catalog:  # Loop through books to find the one being returned.
        if book.id == book_id:
            if not book.borrowed:  # 'not' to check if the book isn't borrowed.
                print(f"Book '{book.title}' was not borrowed.")
                return
            book.borrowed = False  # Mark the book as returned.
            book.borrower = None  # Remove the borrower.
            print(f"Book '{book.title}' returned successfully.")
            return
    print(f"No book found with ID: {book_id}")  # 'else' block for no match.

def delete_book(book_id):
    for i, book in enumerate(global_library_catalog):  # 'for' loop with enumerate to find the index.
        if book.id == book_id:
            del global_library_catalog[i]  # 'del' keyword to remove the book from the catalog.
            print(f"Deleted book with ID: {book_id}")
            break  # 'break' keyword to exit the loop once the book is deleted.
    else:
        print(f"No book found with ID: {book_id}")  # 'else' block when no match is found.

def search_books(keyword):
    found = False  # Variable to track if any books match the search.
    for book in global_library_catalog:  # Loop through the catalog to search for the book.
        if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
            print(book)
            found = True
    if not found:  # 'if' check to print if no matching books were found.
        print("No matching books found.")

def save_catalog(filename="library_catalog.json"):
    try:
        with open(filename, 'w') as file:  # 'with' keyword to open file safely.
            data = [book.__dict__ for book in global_library_catalog]  # Convert books to dictionaries.
            json.dump(data, file)  # Writing to JSON file.
        print("Library catalog saved.")
    except Exception as e:  # Catching exceptions during the file operation.
        print("Error saving catalog:", e)
    finally:  # 'finally' block will always execute, regardless of an error.
        print("Save attempt finished.")

def load_catalog(filename="library_catalog.json"):
    global global_book_id
    try:
        with open(filename, 'r') as file:  # 'with' to safely open file for reading.
            data = json.load(file)  # Reading JSON file.
            for item in data:
                book = Book(item['title'], item['author'])
                book.id = item['id']
                book.borrowed = item['borrowed']
                book.borrower = item['borrower']
                global_library_catalog.append(book)
            if data:  # Checking if there is any data loaded from the file.
                global_book_id = max(item['id'] for item in data)  # Set the global book ID to the highest one.
        print("Library catalog loaded.")
    except FileNotFoundError:  # Exception handling when file is not found.
        print("No catalog found to load.")
    except Exception as e:
        print("Error loading catalog:", e)
    finally:  # 'finally' block ensures this runs regardless of exceptions.
        print("Load attempt finished.")

def late_return_checker(due_date):
    today = dt.now().date()  # Current date.
    due = dt.strptime(due_date, "%Y-%m-%d").date()  # Convert due date string to date object.

    if today > due:  # Checking if today's date is later than the due date.
        days_late = (today - due).days  # Calculate how many days late.
        print(f"Return is late by {days_late} days!")
        return True
    else:
        print("Returned on time.")
        return False

# Demonstrating yield
def available_books():
    for book in global_library_catalog:  # 'for' loop to iterate through books.
        if not book.borrowed:  # 'not' to check if the book is not borrowed.
            yield book  # 'yield' keyword to generate available books one by one.

# Demonstrating nonlocal
def counter():
    count = 0  # Local variable `count` for counting actions.
    def increment():
        nonlocal count  # 'nonlocal' to modify the variable in the enclosing scope.
        count += 1
        return count
    return increment  # Returning the increment function.

# Placeholder function demonstrating pass
def future_feature():
    pass  # 'pass' keyword for a function that's not implemented yet.

# Raise example
def raise_example():
    raise Exception("This is a custom exception!")  # 'raise' keyword to throw an exception.

# Main menu with control flow
def main_menu():
    print("Welcome to the Library Management System")
    load_catalog()  # Load the catalog at the start.

    action_counter = counter()  # Calling the counter function to track actions.

    while True:  # 'while' loop to keep the menu running.
        print("\nAvailable actions:")
        print("1. Add Book")
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Delete Book")
        print("6. Search Book")
        print("7. Show Available Books (using yield)")
        print("8. Save Catalog")
        print("9. Exit")

        choice = input("Choose an action: ")

        if choice == '1':  # 'if' block to add a book.
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)

        elif choice == '2':  # 'elif' block to list all books.
            list_books()

        elif choice == '3':  # 'elif' block to borrow a book.
            member_name = input("Enter member name: ")
            book_id = int(input("Enter book ID to borrow: "))
            borrow_book(member_name, book_id)

        elif choice == '4':  # 'elif' block to return a book.
            book_id = int(input("Enter book ID to return: "))
            return_book(book_id)

            # Optional late return check
            due_date = input("Enter due date (YYYY-MM-DD): ")
            if due_date:
                late_return_checker(due_date)

        elif choice == '5':  # 'elif' block to delete a book.
            book_id = int(input("Enter book ID to delete: "))
            delete_book(book_id)

        elif choice == '6':  # 'elif' block to search for a book.
            keyword = input("Enter keyword to search: ")
            search_books(keyword)

        elif choice == '7':  # 'elif' block to show available books.
            print("Available books:")
            for book in available_books():  # Using the yield-based function to show available books.
                print(book)

        elif choice == '8':  # 'elif' block to save the catalog.
            save_catalog()

        elif choice == '9':  # 'elif' block to exit the program.
            print("Exiting Library Management System...")
            save_catalog()
            break  # 'break' to exit the loop.

        else:
            print("Invalid choice. Try again.")
            continue  # 'continue' to skip this iteration and prompt again.

        # Assert example
        assert len(global_library_catalog) >= 0, "Catalog can't have negative books!"  # 'assert' to ensure no negative books.

        # Lambda example
        book_titles = list(map(lambda b: b.title, global_library_catalog))  # 'lambda' to extract book titles.
        print("Book titles in library:", book_titles)

        # Example of and / or / is / not
        if len(global_library_catalog) > 0 and action_counter() > 0:  # 'and' to check if both conditions are true.
            print("Actions performed:", action_counter())
        elif len(global_library_catalog) == 0 or action_counter() == 0:  # 'or' to check if either condition is true.
            print("Library is empty or no actions taken.")

if __name__ == "__main__":  # 'if' block to ensure the script is executed directly.
    main_menu()  # Calling the main menu function to start the program.
