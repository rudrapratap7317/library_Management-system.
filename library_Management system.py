# LIBRARY MANAGEMENT SYSTEM

books = []

# Function to add a book
def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "name": book_name,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    print("Book Added Successfully!")


# Function to view all books
def view_books():
    if len(books) == 0:
        print("No Books Available")
    else:
        for book in books:
            print("--------------------")
            print("Book ID:", book["id"])
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            print("Status:", book["status"])


# Function to search a book
def search_book():
    book_id = input("Enter Book ID to Search: ")

    for book in books:
        if book["id"] == book_id:
            print("Book Found!")
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            print("Status:", book["status"])
            return

    print("Book Not Found")


# Function to issue a book
def issue_book():
    book_id = input("Enter Book ID to Issue: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                book["status"] = "Issued"
                print("Book Issued Successfully!")
            else:
                print("Book is Already Issued")
            return

    print("Book Not Found")


# Function to return a book
def return_book():
    book_id = input("Enter Book ID to Return: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                book["status"] = "Available"
                print("Book Returned Successfully!")
            else:
                print("Book is Already Available")
            return

    print("Book Not Found")


# Main Program
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again")